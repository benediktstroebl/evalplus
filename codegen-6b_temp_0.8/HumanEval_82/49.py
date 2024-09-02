
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Is the number a perfect square?
    if is_square(int(len(string))):
        return False

    # Check for prime numbers
    for i in range(2, int(len(string))+1):
        if is_prime(i):
            if is_permutation(string, string[:i]):
                return True
    return False
