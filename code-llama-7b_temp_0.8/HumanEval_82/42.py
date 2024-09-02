
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    prime = lambda x: all(x % i != 0 for i in range(2, x))

    if prime(len(string)):
        return True
    else:
        return False

