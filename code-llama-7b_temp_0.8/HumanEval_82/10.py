
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string = len(string)
    if string == 2 or string == 3 or string == 5 or string == 7:
        return True
    elif string == 4 or string == 6 or string == 8 or string == 9:
        return False
    elif string == 1:
        return False
    elif string % 2 == 0 or string % 3 == 0 or string % 5 == 0 or string % 7 == 0:
        return False
    else:
        return True
