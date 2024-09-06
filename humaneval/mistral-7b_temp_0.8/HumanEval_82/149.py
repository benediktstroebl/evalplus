
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    import math
    if len(string) == 1:
        return True
    elif len(string) == 2:
        return True
    elif len(string) % 2 == 0:
        return False
    else:
        sq_root = int(math.sqrt(len(string)))
        for i in range(3, sq_root + 1, 2):
            if len(string) % i == 0:
                return False
            else:
                return True

