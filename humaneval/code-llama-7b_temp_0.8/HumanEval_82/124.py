
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Turn the string into a list
    string = list(string)

    # Check to see if the string is empty
    if not string:
        return False

    # Length of the string
    string_length = len(string)

    # Prime factors
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Return True if the length of the string is one of the prime factors
    if string_length in primes:
        return True
    else:
        return False























