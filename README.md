# Conexão com banco de dados

SO Utilizado: Windows 10 PRO

============ PROGRAMAS RECOMENDADOS ============

IDE: VSCode

Python: Versão 3.10.7

SQL Server: Versão 19.0.1

MySQL: Versão 8.0.36

PostgreSQL: Versão 14

============ ORIENTAÇÕES ============

1- Crie um ambiente virtual na raiz do projeto utilizando o comando abaixo no terminal do VSCode:

python -m venv venv

2- Ative o ambiente virtual usando o comando abaixo no terminal do VSCode:

.\venv\Scripts\Activate.ps1

OBSERVAÇÃO: Se seu SO não for windows e sua IDE não for o VSCode, procure como são feitas as etapas 1 e 2 para sua necessiade.

OBSERVAÇÃO: Antes de executar o passo 3, tenha certeza que seu ambiente virutal está ativo, após executar o comando do passo 2, verifique se ao lado do caminho do seu terminal no VSCode possui a identificação (venv)

![caminho](https://github.com/mateusdev08/python-classe-conexao-banco-de-dados/assets/140756008/5711577b-b47c-48c5-98f8-67c2f496363c)

3- Com o ambiente virtual ativo, instale as bibliotecas necessárias utilizando o arquivo requirements.txt executando o comando abaixo:

pip install -r requirements.txt

4- Configure o arquivo .env_template com as credenciais do seu banco de dados e renomeie o arquivo para .env

5- Adapte as consultas do arquivo consultas.py conforme a sua necessidade.

6- Caso crie uma nova consulta, não esqueça de importar no arquivo main.py e mostrar o resultado usando print

============ PARA ENTRAR EM CONTATO ============

Linkedin: www.linkedin.com/in/mateus-carmo-da-silva-43675341
