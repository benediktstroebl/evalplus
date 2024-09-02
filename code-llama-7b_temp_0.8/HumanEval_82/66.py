
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # first we get the length of the string
    length = len(string)
    # we create an array to store the prime numbers
    primes = []

    # we start by checking if length is 0, if not we continue
    if length != 0:
        # then we check if length is prime
        if length > 1:
            # if it is, we add it to primes
            primes.append(length)
        # then we check if the length is a prime number
        for i in range(2, length):
            if length % i == 0:
                break
            else:
                primes.append(i)
        # then we check if the length is in primes, if it is, it is prime
        if length in primes:
            return True
        # otherwise, it is not
        return False
    # if length is 0, it is not prime
    return False
