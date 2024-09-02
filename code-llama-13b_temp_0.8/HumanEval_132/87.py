
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    #pass

    #Funcion para comparar la cantidad de corchetes
    def check(string):
        lista=[]
        for i in string:
            if i == "[" or i == "]":
                lista.append(i)
        if lista.count("[") == lista.count("]"):
            return True
        else:
            return False

    #Funcion para comparar las posiciones de los corchetes
    def compare(string):
        lista=[]
        for i in string:
            if i == "[" or i == "]":
                lista.append(i)
        n=1
        k=0
        for i in range(len(lista)):
            if lista[i] == "[":
                n += 1
            elif lista[i] == "]":
                n -= 1
            if n == 0:
                k+=1
        if k == lista.count("]"):
            return True
        else:
            return False
    
    #Funcion para devolver el booleano
    if check(string)==True and compare(string)==True:
        return True
    else:
        return False


    
