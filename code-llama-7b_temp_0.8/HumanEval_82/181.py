
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    #my_string = string.replace('a', 'b')
    #my_string = string.replace('e', 'f')
    #my_string = string.replace('i', 'j')
    #my_string = string.replace('o', 'p')
    #my_string = string.replace('u', 'v')
    #print(my_string)
    #my_string = my_string.replace('b', 'a')
    #my_string = my_string.replace('f', 'e')
    #my_string = my_string.replace('j', 'i')
    #my_string = my_string.replace('p', 'o')
    #my_string = my_string.replace('v', 'u')
    #print(my_string)
    #return False
    # if string_length % 2 == 0:
    #     return True
    # else:
    #     return False
    #if not string_length % 2 == 0:
    #    return True
    #else:
    #    return False
    string_length = len(string)
    for i in range(2, string_length):
        if string_length % i == 0:
            return False
    return True




