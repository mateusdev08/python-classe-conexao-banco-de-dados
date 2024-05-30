import sqlite3 as con_lite
import pyodbc as con_server
import mysql.connector as con_mysql
import psycopg2 as con_postgre
import os
from dotenv import load_dotenv

load_dotenv()


class Conexao:
    """Modo de usar:

    1- Para utilizar a classe, crie uma instância

    conexao = Conexao()

    2- Para utilizar o SQLite

    conexao.conectar_sqlite

    cursor.execute('instrução SQL')

    conexao.desconectar_sqlite

    3- Para utilizar o SQL Server

    conexao.conectar_sql_server

    cursor.execute('instrução SQL')

    conexao.desconectar_sql_server

    4- Para utilizar o MySQL

    conexao.conectar_mysql

    cursor.execute('instrução SQL')

    conexao.desconectar_mysql

    5- Para utilizar o Postgre

    conexao.conectar_postgre

    cursor.execute('instrução SQL')

    conexao.desconectar_postgre
    """
    @property
    def conectar_sqlite(self):
        self.conexao_lite = con_lite.connect('db.sqlite3')
        self.cursor_lite = self.conexao_lite.cursor()
        print('Conectado no SQLite.')

    @property
    def desconectar_sqlite(self):
        self.cursor_lite.close()
        self.conexao_lite.close()
        print('Desconectado do SQLite.')

    @property
    def conectar_sql_server(self):

        server = os.getenv('SQL_SERVER_HOST')
        database = os.getenv('SQL_SERVER_DB')
        username = os.getenv('SQL_SERVER_UID')
        password = os.getenv('SQL_SERVER_PWD')

        dados = f"DRIVER={'{SQL Server}'};SERVER={server};DATABASE={database};UID={username};PWD={password}"

        self.conexao_sql_server = con_server.connect(dados)
        self.cursor_sql_server = self.conexao_sql_server.cursor()
        print('Conectado no SQL Server.')

    @property
    def desconectar_sql_server(self):
        self.cursor_sql_server.close()
        self.conexao_sql_server.close()
        print('Desconectado do SQL Server.')

    @property
    def conectar_mysql(self):

        dados = {
            'host': os.getenv('MYSQL_HOST'),
            'port': os.getenv('MYSQL_PORT'),
            'user': os.getenv('MYSQL_UID'),
            'password': os.getenv('MYSQL_PWD'),
            'database': os.getenv('MYSQL_DB')
        }

        self.conexao_mysql = con_mysql.connect(**dados)
        self.cursor_mysql = self.conexao_mysql.cursor()
        print('Conectado no MySQL.')

    @property
    def desconectar_mysql(self):
        self.cursor_mysql.close()
        self.conexao_mysql.close()
        print('Desconectado do MySQL.')

    @property
    def conectar_postgre(self):

        dados = {
            'host': os.getenv('POSTGRE_HOST'),
            'database': os.getenv('POSTGRE_DB'),
            'user': os.getenv('POSTGRE_UID'),
            'password': os.getenv('POSTGRE_PWD'),
            'port': os.getenv('POSTGRE_PORT')
        }

        self.conexao_postgre = con_postgre.connect(**dados)
        self.cursor_postgre = self.conexao_postgre.cursor()
        print('Conectado no Postgre.')

    @property
    def desconectar_postgre(self):
        self.cursor_postgre.close()
        self.conexao_postgre.close()
        print('Desconectado do Postgre.')
