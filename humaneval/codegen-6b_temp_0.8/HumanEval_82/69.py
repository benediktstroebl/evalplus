
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # convert to lower case
    string = string.lower()
    # first pass: is the string length divisible by 2?
    if len(string)%2 == 0:
        return False
    # second pass: is the nth character a prime number?
    # list of primes
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
    for prime in primes:
        if string[round(len(string)/2)] == str(prime):
            return True
    # in case the string isn't divisible by 2
    return False
