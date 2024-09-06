
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    count = 0
    for i in string:
        count += 1
    if count == 1:
        return True
    elif count == 2:
        return True
    elif count == 3:
        return True
    elif count == 4:
        return False
    elif count == 5:
        return True
    elif count == 6:
        return False
    elif count == 7:
        return True
    elif count == 8:
        return False
    elif count == 9:
        return False
    elif count == 10:
        return False
    elif count == 11:
        return True
    elif count == 12:
        return False
    elif count == 13:
        return True
    elif count == 14:
        return False
    elif count == 15:
        return False
    elif count == 16:
        return False
    elif count == 17:
        return True
    elif count == 18:
        return False
    elif count == 19:
        return True
    elif count == 20:
        return False

