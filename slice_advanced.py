def slice_advanced():
# Código a implementar utilizando input.
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
    
    x = "Awesome"
    x_real = x.lower()

    print(x_real [:3])    #Imprime las 3 primera letras del texto

    mitad = int(len(x_real)/2)      #me dice cual es la mitad del texto // El int me quita la parte fraccional, no redondea
    print(x_real [mitad - 1 : mitad + 2])      #DESDE mitad-2 HASTA mitad+1

    print(x_real[ :4] + x[-3: ])
