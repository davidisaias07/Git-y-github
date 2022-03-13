
def menu (tipo_plato,precio):
    print("Elegiste " + tipo_plato+", el precio de: " + str(precio)+ " soles")


platos_comida = """ Bievenido al menú, te presentamos nuestros platos disponibles:

1- Arroz con papas
2- Fideos al alfredo
3- Tallarines rojos con carne
4- Plato oculto

"""

platos_comida = int(input("""Bievenido al menú, te presentamos nuestros platos disponibles:

1- Arroz con pollo
2- Fideos al alfredo
3- Tallarines rojos con carne
4- Plato oculto
Elije una opción: """))


if platos_comida == 1:
    menu("arroz con papas", 14)

elif platos_comida == 2:
    menu("fideos al alfredo", 17)

elif platos_comida == 3:
    menu("tallarines rojos con carne", 12.5)

elif platos_comida == 4:
    print("Plato oculto está disponible solo los viernes")

else:
    while platos_comida > 4:
        print("Elegiste una opcion mayor a 5, vuelve a intentarlo")
        break
    



