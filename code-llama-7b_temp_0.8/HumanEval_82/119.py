
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    x = len(string)
    n = 1
    while n < x:
        if x % n == 0:
            return False
        else:
            n += 1
    return True


