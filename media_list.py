def recebe_numeros(lista):
	if len(lista) <= 2 or not lista:
		return None

	maxv = max(lista) 
	lista.remove(maxv)
	minv = min(lista)
	lista.remove(minv)

	resul = sum(lista) / len(lista)
	return resul

listav = list(range(2134))
print('O digito que você escolheu dividido sem o maior e o menor número é: ' ,recebe_numeros(listav))