
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    prime_length = len(string)
    if prime_length > 1:
        for i in range(2, prime_length):
            if prime_length % i == 0:
                return False
            else:
                return True
    else:
        return False

