
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # prime numbers are only those that are less than n-1, because the
    # next prime number will have n factors
    # therefore, we can stop checking when the number is less than the square root
    n = int(len(string) ** 0.5)
    for i in range(2, n+1):
        if string[0] * string[1] * string[2] * string[3] % i == 1:
            return True
    return False
