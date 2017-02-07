import mysql.connector

# ----Classe responsavel por gerenciar o mysql e o Crud-----
class Conexao(object):

	# Metodo para abrir conexao
	def abrirConexao(self):
		config = {
		'user'             : 'root',
		'password'         : '',
		'host'             : 'localhost',
		'database'         : 'crudpython',
		'raise_on_warnings': True,
		}
		self.conexao = mysql.connector.connect(**config)

		return self.conexao

	# Metodo para fechar conexao
	def fecharConexao(self):
		self.conexao.close();

	# Metodo para inserir dados na tabela contatos
	def addContatoNoBanco(self,data_contato):
		cursor = self.conexao.cursor()

		add_contato = ("INSERT INTO contatos "
			         "(primeiro_nome,segundo_nome,telefone_um,telefone_dois,endereco,email) VALUES"
			         "(%(primeiro_nome)s,%(segundo_nome)s,%(telefone_um)s,%(telefone_dois)s,%(endereco)s,%(email)s)")


		cursor.execute(add_contato,data_contato)
		self.conexao.commit()

		cursor.close()

def receberDadosNovoContato():
	print("Insira um novo contato")

	# Lista que recebe os dados do novo contato
	contato = []

	contato.append(input("Primeiro Nome: "))
	contato.append(input("Segundo Nome: "))
	contato.append(input("Primeiro Telefone: "))
	contato.append(input("Segundo Telefone: "))
	contato.append(input("Endereço: "))
	contato.append(input("Email: "))
	
	# Caso o campo esteja vazio ele recebe valor DEFAULT
	i = 0
	for dado in contato:
		if dado == '':
			contato[i] = None
		i=+1

	# retorna json com informações do contato
	novoContato = {
		'primeiro_nome' : contato[0],
		'segundo_nome'  : contato[1],
		'telefone_um'   : contato[2],
		'telefone_dois' : contato[3],
		'endereco'      : contato[4],
		'email'         : contato[5]
	}
	return novoContato


	# Metodo para visualisar Contatos
	# def verContatos(self):
	# 	cursor = self.cone

# --------Metodo Responsavel por rodar a aplicação
def main():
	conexao  = Conexao()
	conexao.abrirConexao()

	print("Bem Vindo ao ContateShell-V-Py\n")
	
	conexao.addContatoNoBanco(receberDadosNovoContato())

	conexao.fecharConexao()


# Chamando main() para rodar a aplicação
main()