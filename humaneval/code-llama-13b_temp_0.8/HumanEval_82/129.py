
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    n = len(string)
    c = 0
    if n == 0 or n == 1:
        return False
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

