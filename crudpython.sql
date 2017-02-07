-- Apagando e Criando Banco
DROP SCHEMA IF EXISTS crudpython;
CREATE SCHEMA IF NOT EXISTS crudpython;

-- Criando Tabela Contatos
CREATE TABLE IF NOT EXISTS crudpython.contatos(
	id INT(3) AUTO_INCREMENT PRIMARY KEY,
	primeiro_nome VARCHAR(50) NOT NULL,
	segundo_nome VARCHAR(50),
	telefone_um VARCHAR(14) NOT NULL,
	telefone_dois VARCHAR(14),
	endereco VARCHAR(50),
	email VARCHAR(30)
);

-- Inserindo dados na tabela Contatos
INSERT INTO crudpython.contatos(primeiro_nome,segundo_nome,telefone_um)
VALUES
	('Blade','Baiano','(21)0000-23232'),
	('FW','Santos','(99)11122-3333'),
	('McFly',DEFAULT,'FUTURE')
;

--Visualizar o resultado
SELECT * FROM crudpython.contatos;