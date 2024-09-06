
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    from math import sqrt
    s = len(string)
    s = s // 2

    if s < 2:
        return True
    elif s == 2:
        return False
    elif s % 2 == 0:
        return False
    else:
        for i in range(2, int(sqrt(s)) + 1):
            if s % i == 0:
                return False
    return True

