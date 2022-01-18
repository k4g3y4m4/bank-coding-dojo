class accountbank:
    name = "Interbank"
    accountsbank = []
    def __init__(self, tasa_interés, balance): 
        self.tasa_interés = tasa_interés
        self.balance = balance
        accountbank.accountsbank.append(self)

    def depósito(self, amount): 

        self.balance += amount
        return self

    def retiro(self, amount):
        self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: {self.balance}")

    def generar_interés(self):
        self.balance += self.balance * self.tasa_interés
        return self
    
    def gettasa_interés(self):
        return self.tasa_interés

    def getbalance(self):
        return self.balance

    def setbalance(self, balance):
        self.balance = balance
    
    def settasa_interés(self, tasa_interés):
        self.tasa_interés = tasa_interés

    def __repr__(self):
        return f"{self.balance}"

class user:
    users = []
    def __init__(self,name):
        self.name = name
        self.email = name.lower() + "@gmail.com"
        self.account = accountbank(0.01,0)
        self.accountsuser = []
        self.accountsuser.append(self.account)
        user.users.append(self)

    def mostrar_info_usuario(self):
        print(f"Nombre: {self.name}")
        print(f"Email: {self.email}")
        print(f"Cuentas: {self.accountsuser.__repr__()}")
        self.account.mostrar_info_cuenta()

    def crear_cuenta_nueva(self):
        account = accountbank(0.01,0)
        self.accountsuser.append(account)
        print("Cuenta creada con éxito")
        return self

    def hacer_deposito(self, amount):
        for i in range(0,len(self.accountsuser)):
            print(f"Cuenta bancaria {i+1}: Balance {self.accountsuser[i]}")
        print(f"Cuenta a la que desea hacer el depósito: ")
        account = int(input())
        self.accountsuser[account-1].depósito(amount)
        print(f"Depósito realizado con éxito")
        return self

    def hacer_retiro(self, amount):
        for i in range(0,len(self.accountsuser)):
            print(f"Cuenta bancaria {i+1}: Balance {self.accountsuser[i]}")
        print(f"Cuenta a la que desea hacer el retiro: ")
        account = int(input())
        if(self.accountsuser[account-1].getbalance() < amount):
            print("No tiene suficiente saldo")
        else:
            self.accountsuser[account-1].retiro(amount)
            print(f"Retiro realizado con éxito")
        return self
    
    def mostrar_balance(self):
        print("Balance de cuentas")
        print("-------------------")
        for i in range(0,len(self.accountsuser)):
            print(f"Cuenta bancaria {i+1} - {self.accountsuser[i].getbalance()}")
        return self


