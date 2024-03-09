def welcome_message():
		name = input("Por favor ingrese su nombre: ")
		atencion = input("Que fue lo que mas te llamo la atencion del curso: ")
		print("Bienvenido,", name, "al curso de Django y React!")
		print("Espero que aprendas", atencion)
														
if __name__ == "__main__":
	welcome_message()