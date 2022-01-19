from classes import KTY, TINT, FTMI, FTMF, NOZHiBtins
kty=KTY(4)
tint=TINT(2)
ftmi=FTMI(1)
ftmf=FTMF(3)
nozhibtins=NOZHiBtins(5)
kty.iteraction(4)
tint.iteraction(2)
ftmi.iteraction(100500)
ftmf.iteraction('сгорела')
nozhibtins.iteraction('пиво')
megafaculties=[kty,tint,ftmi,ftmf,nozhibtins]
for megafaculty in megafaculties:
    megafaculty.show_info()
kty+=tint
print(f'Всего в ИТМО {kty} факультетов учатся на программистов')
input()
