def welcome_message():
		name = input("Por favor ingrese su nombre: ")
		ciudad = input("Por favor agregue su ciudad: ")
		print("Bienvenido,", name, "al curso de Django y React!")
		print("Espero te encuentre bien en", ciudad)
														
if __name__ == "__main__":
	welcome_message()