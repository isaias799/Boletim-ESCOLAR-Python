lista = []

while  True:
    name = str(input('NOME: '))
    nota1 = float(input('1º NOTA: '))
    nota2 = float(input('2º NOTA: '))
    média = (nota1 + nota2) / 2
    lista.append([name, [nota1, nota2], média])
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('-=-' * 15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=' * 25)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=-' * 15)
    opç = int(input('Mostrar notas de qual aluno ("999" interrompe):' ))
    if opç == 999:
        print('FINALIZANDO')
        break
    if opç <= len(lista) - 1:
        print(f'Notas de {lista[opç][0]} são {lista[opç][1]}')
print('<<<<< VOLTE SEMPRE >>>>>')
