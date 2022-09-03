import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='admin',
    password='1234',
    database='firstbd'
)
cursor = conexao.cursor()

# Create
nome_produto = "Coca"
valor = 4
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() # edita o banco de dados
resultado = cursor.fetchall() # ler o banco de dados


# Read
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

# Update
nome_produto = "toddynho"
valor = 5
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

#Delete
nome_produto = "Sorvete"
comando = f'DELETE from vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

cursor.close() 
conexao.close()
