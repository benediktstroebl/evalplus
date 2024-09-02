
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
    num = len(string)
    if num == 1:
        return True
    if num > 1 and num % 2 == 0:
        return False
    i = 3
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i += 2
    return True
