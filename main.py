char_proibidos = [":", "-", "+", "|", "/", "?"]

#abrir o código jvs
def abrir_arq(nome, pad = "r"):
	with open(nome,pad,encoding="utf-8") as arq:
		text = arq.read()
	return text

def checar_char_proibido(x):
	t = True
	for i in x:
		if i in char_proibidos:
			t = False

	return t

def In(a, b):
	return a in b

def checar_variaveis(x, variaveis):
	t = False
	for i in variaveis.keys():
		if In(i, x):
			if x[0] != '"' and x[-1] != '"':
				t = True

	return t

def declarar_variavel(code, variaveis):
	code = code.split(" é do tipo ")
	if code[1] == "inteiro":
		variaveis.update({code[0]:{"tipo": "inteiro", "valor": 0}})

def diga(code, variaveis):
	try:
		code = code.strip("Diga: ")
		code = code.split(";")
	except:
		print('Para iniciar o comando "Diga" é necessário escrever "Diga: ", tendo u espaço depois mesmo')
		exit()
	for i in code:
		if not In(" ", i):
			if checar_variaveis(code, variaveis) and checar_char_proibido(i):
				print(variaveis[i]["valor"], end="")
			else: 
				print(i, end = "")
		else:
			print(i, end = "")
	print()
	

def dar_valor(code, variaveis):
	code = code.split(" é igual a ")
	if code[0] in variaveis.keys():
		try:
			variaveis[code[0]]["valor"] = int(code[1])
		except:
			print("Esse valor não é inteiro")
			exit()
	else:
		print("Essa variável não foi declarada")
		exit()

def somar_valor(code, variaveis):
	a = 0
	b = 0
	
	code = code.split(" é igual a soma de ")
	code[1] = code[1].split(" mais ")
	
	if code[0] in variaveis.keys():
		a = code[1][0]
		b = code[1][1]

		if variaveis[code[0]]["tipo"] == "inteiro":
			try:
				a = int(a)
			except:
				if a in variaveis.keys():
					a = variaveis[a]["valor"]
				else:
					print("Essa variável não existe")

			try:
				b = int(b)
			except:
				if b in variaveis.keys():
					b = variaveis[b]["valor"]
				else:
					print("Essa variável não existe")

	else:
		print("Essa variável não existe")

	variaveis[code[0]]["valor"] = a + b

def subtracao_valor(code, variaveis):
	a = 0
	b = 0
	
	code = code.split(" é igual a subtração de ")
	code[1] = code[1].split(" menos ")
	
	if code[0] in variaveis.keys():
		a = code[1][0]
		b = code[1][1]

		if variaveis[code[0]]["tipo"] == "inteiro":
			try:
				a = int(a)
			except:
				if a in variaveis.keys():
					a = variaveis[a]["valor"]
				else:
					print("Essa variável não existe")

			try:
				b = int(b)
			except:
				if b in variaveis.keys():
					b = variaveis[b]["valor"]
				else:
					print("Essa variável não existe")

	else:
		print("Essa variável não existe")

	variaveis[code[0]]["valor"] = a - b

def main():
	#abrindo código jvs
	code = abrir_arq("teste.ptbrl").split("\n")
	#print(code)
	
	#definindo váriaveis
	variaveis = {}
	loop = False
	
	for i in code:
		if i != "" and i[0:5] != "Obs: ":
			if i[-1] != ".":
				print("esqueceu do ponto")
				exit()
			elif In("se", i):
				print("sucess")
				
			elif In("A variável", i):
				declarar_variavel(i[11:-1], variaveis)
				
			elif In("é igual a soma", i):
				somar_valor(i.strip("."), variaveis)

			elif In("é igual a subtração", i):
				subtracao_valor(i.strip("."), variaveis)
			
			elif In("é igual", i):
				dar_valor(i.strip("."), variaveis)

			elif In("Diga", i):
				diga(i.strip("."), variaveis)
	
	
	return 0
	
if __name__=="__main__":
	main()
