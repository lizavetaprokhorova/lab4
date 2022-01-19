class ITMO():
    def __init__(self, snumber):
        self.snumber = snumber

    def street_name(self):
        self.name = "Lomonosovskaia"
        return f"{self.name} street, "

    def show_info(self):
        print(f"{self} находится на {self.street_name()}корпус {self.snumber}")

class KTY(ITMO):
    def __str__(self):
        return'КТиУ'

    def iteraction(self,iteraction):
        self.iteraction=iteraction
        print(f'На КТиУ {self.iteraction} факультета')

class TINT(ITMO):
    def __str__(self):
        return 'ТИНТ'

    def iteraction(self,iteraction):
        self.iteraction=iteraction
        print(f'На ТИНТе {self.iteraction} факультета')

class FTMI(ITMO):
    def __str__(self):
        return 'ФТМИ'

    def iteraction(self,iteraction):
        self.iteraction=iteraction
        print(f'ФТМИ потратили {self.iteraction} денег на мегабаттл')

class FTMF(ITMO):
    def __str__(self):
        return 'ФТМФ'

    def iteraction(self,iteraction):
        self.iteraction=iteraction
        print(f'Фотоника {self.iteraction} уже до тла')

class  NOZHiBtins(ITMO):
    def __str__(self):
        return 'НОЖиБтинс'

    def iteraction(self,iteraction):
        self.iteraction=iteraction
        print(f'Бтинс варят {self.iteraction}')

