userInput = input('Digite algo: ')
print('Tipo: {}'.format(type(userInput)))
print('É numérico: {}'.format(userInput.isnumeric()))
print('É decimal: {}'.format(userInput.isdecimal()))
print('É alfa: {}'.format(userInput.isalpha()))
print('É alfanumérico: {}'.format(userInput.isalnum()))
print('É espaço: {}'.format(userInput.isspace()))
print('É Ascii: {}'.format(userInput.isascii()))
print('É Dígito: {}'.format(userInput.isdigit()))
print('Somente letras maiúsculas: {}'.format(userInput.isupper()))
print('Somente letras minúsculas: {}'.format(userInput.islower()))
print('Capitalizada: {}'.format(userInput.istitle()))
