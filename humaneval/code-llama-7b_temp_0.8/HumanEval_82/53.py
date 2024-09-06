
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # if not prime:
    #     return False
    # return True
    # if not isinstance(string, str):
    #     raise TypeError("Not a valid type")
    # if string == '':
    #     return False
    # if len(string) == 1 or len(string) == 2:
    #     return False
    # if len(string) % 2 == 0 or len(string) % 3 == 0:
    #     return False
    # return True

    # if not string:
    #     return False
    # if len(string) == 1 or len(string) == 2:
    #     return False
    # if len(string) % 2 == 0 or len(string) % 3 == 0:
    #     return False
    # return True

    # if not string or len(string) == 1 or len(string) == 2:
    #     return False
    # if len(string) % 2 == 0 or len(string) % 3 == 0:
    #     return False
    # return True

    if not string:
        return False
    if len(string) == 1 or len(string) == 2:
        return False
    if len(string) % 2 == 0 or len(string) % 3 == 0:
        return False
    return True


