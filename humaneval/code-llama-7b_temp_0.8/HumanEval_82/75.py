
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return True
    elif len(string) == 2:
        return True
    elif len(string) == 3:
        return True
    elif len(string) == 4:
        return False
    elif len(string) == 5:
        return False
    elif len(string) == 6:
        return False
    elif len(string) == 7:
        return False
    elif len(string) == 8:
        return False
    elif len(string) == 9:
        return False
    elif len(string) == 10:
        return False
    else:
        return True
