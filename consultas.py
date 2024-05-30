from mod_db import Conexao
import pandas as pd

# Instância de conexão
conexao = Conexao()

# Conexões com banco de dados
conexao.conectar_sql_server
conexao.conectar_mysql
conexao.conectar_postgre

# Consultas SQL
df_1 = pd.read_sql('SELECT * FROM DIM_FLUXO_CONTA', conexao.conexao_sql_server)
df_2 = pd.read_sql('select * from cartao;', conexao.conexao_mysql)
df_3 = pd.read_sql('select * from natju;', conexao.conexao_postgre)

# Desconectar banco de dados
conexao.desconectar_sql_server
conexao.desconectar_mysql
conexao.desconectar_postgre
