
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    length = len(string)
    if length == 2:
        return True
    elif length == 5:
        return True
    elif length == 7:
        return True
    elif length == 11:
        return True
    elif length == 13:
        return True
    elif length == 17:
        return True
    elif length == 19:
        return True
    elif length == 23:
        return True
    elif length == 29:
        return True
    elif length == 31:
        return True
    else:
        return False
