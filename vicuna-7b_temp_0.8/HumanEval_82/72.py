
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # The above code is a simple implementation of the Sieve of Eratosthenes
    # algorithm, a well-known method for checking if a number is prime.
    #
    # However, this implementation is not very efficient and will not work
    # for large numbers.  A better solution is to use a more efficient algorithm
    # such as the Miller-Rabin primality test.

    # This implementation is intended to serve only as a simple example
    # of how to implement the algorithm in Python.

    # Note that the string must be converted to an integer in order to
    # check for primality.
    if len(string) == 1 or len(string) == 2 or len(string) == 3:
        return True
    else:
        for i in range(2, int(math.sqrt(len(string))) + 1):
            if string[i] == '1':
                return False
        return True
