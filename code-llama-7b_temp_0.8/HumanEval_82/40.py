
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if not string:
        return False
    if len(string) == 1:
        return True
    if len(string) == 2:
        return True
    if len(string) % 2 == 0:
        return False
    if len(string) == 3:
        return True
    if len(string) % 3 == 0:
        return False
    if len(string) == 5:
        return True
    if len(string) % 5 == 0:
        return False
    if len(string) == 7:
        return True
    if len(string) % 7 == 0:
        return False
    if len(string) == 11:
        return True
    if len(string) % 11 == 0:
        return False
    if len(string) == 13:
        return True
    if len(string) % 13 == 0:
        return False
    if len(string) == 17:
        return True
    if len(string) % 17 == 0:
        return False
    if len(string) == 19:
        return True
    if len(string) % 19 == 0:
        return False
    if len(string) == 23:
        return True
    if len(string) % 23 == 0:
        return False
    if len(string) == 29:
        return True
    if len(string) % 29 == 0:
        return False
    if len(string) == 31:
        return True
    if len(string) % 31 == 0:
        return False
    if len(string) == 37:
        return True
    if len(string) % 37 == 0:
        return False
    if len(string) == 41:
        return True
    if len(string) % 41 == 0:
        return False
    if len(string) == 43:
        return True
    if len(string) % 43 == 0:
        return False
    if len(string
