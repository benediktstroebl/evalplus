
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # MY SOLUTION -------------------------------------------------------------
    # return len(string) in [2,3,5,7,11,13,17,19,23,29,31]

    # MY SOLUTION using if...elif...else --------------------------------------
    if len(string) == 2:
        return True
    elif len(string) == 3:
        return True
    elif len(string) == 5:
        return True
    elif len(string) == 7:
        return True
    elif len(string) == 11:
        return True
    elif len(string) == 13:
        return True
    elif len(string) == 17:
        return True
    elif len(string) == 19:
        return True
    elif len(string) == 23:
        return True
    elif len(string) == 29:
        return True
    elif len(string) == 31:
        return True
    else:
        return False







