def welcome_message():
    name = input("Por favor ingrese su nombre: ")
    ciudad = input("¿De dónde eres? ")

    print("Bienvenido,", name, "al curso de Django y React!")



    atencion = input("¿Qué fue lo que más te llamó la atención del curso? ")

if __name__ == "__main__":
    welcome_message()