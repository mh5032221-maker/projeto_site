import psycopg2
from config import Config


def conectar():
    if not Config.DATABASE_URL:
        raise Exception("DATABASE_URL não encontrada. Verifique o arquivo .env")
    return psycopg2.connect(Config.DATABASE_URL)


def criar_tabelas():
    con = conectar()
    cur = con.cursor()

    # ===== USUÁRIOS =====
    cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) UNIQUE NOT NULL,
            senha VARCHAR(255) NOT NULL,
            cargo VARCHAR(30) DEFAULT 'Funcionario'
        )
    """)

    cur.execute("""
        ALTER TABLE usuarios
        ADD COLUMN IF NOT EXISTS cargo VARCHAR(30) DEFAULT 'Funcionario'
    """)

    # ===== CLIENTES =====
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(150),
            cpf VARCHAR(20),
            nascimento DATE,
            telefone VARCHAR(30),
            email VARCHAR(150),
            status VARCHAR(30),
            observacoes TEXT,
            senha_cliente VARCHAR(255)
        )
    """)

    # ===== FINANCEIRO =====
    cur.execute("""
        CREATE TABLE IF NOT EXISTS financeiro (
            id SERIAL PRIMARY KEY,
            descricao VARCHAR(150),
            tipo VARCHAR(20),
            valor NUMERIC(12,2),
            data_lancamento DATE
        )
    """)

    con.commit()
    cur.close()
    con.close()