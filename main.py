from bank import user

user1 = user("Juan")

user1.accountsuser[0].depósito(100).retiro(50).generar_interés()
user1.mostrar_info_usuario()
print("\n")
user1.crear_cuenta_nueva()
user1.mostrar_info_usuario()
user1.hacer_deposito(100)
user1.hacer_retiro(50)
print("\n")
user1.mostrar_balance()