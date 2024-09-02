
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    # declaro una variable 'n' para despues asignarle el valor de la longitud de 'arr'
    n = len(arr)
    # le asigno a 'aux' un arreglo vacio, que luego llene con la informacion que voy sacando de 'arr'
    aux = []
    # Declaro una variable 'i' para despues asignarle el valor de 0
    i = 0

    # Comienzo a recorrer el arreglo 'arr' de forma ascendente
    while i < n:
        # Se comprueba que el elemento actual del arreglo 'arr' se encuentre entre 1 y 9
        if arr[i] >= 1 and arr[i] <= 9:
            # Se agrega al arreglo 'aux' el elemento que se encuentra en la posicion de 'i' del arreglo 'arr'
            aux.append(arr[i])
            # Se incrementa en uno la variable 'i'
            i += 1
        # En caso contrario, la variable 'i' pasa a la siguiente iteracion
        else:
            i += 1
    
    # Se ordena el arreglo 'aux' de forma descendente
    aux.sort(reverse=True)

    # Se le asigna la cantidad de elementos que posee el arreglo 'aux' a la variable 'n'
    n = len(aux)
    # Se crea un arreglo vacio para guardar el resultado final
    result = []
    # Se declara una variable 'i' para despues asignarle el valor de 0
    i = 0
    
    # Comienzo a recorrer el arreglo 'aux' de forma ascendente
    while i < n:
        # En caso de que el elemento actual del arreglo 'aux' sea igual a 1
        if aux[i] == 1:
            # Se agrega al arreglo 'result' la palabra 'One'
            result.append('One')
        # En caso de que el elemento actual del arreglo 'aux' sea igual a 2
        elif aux[
