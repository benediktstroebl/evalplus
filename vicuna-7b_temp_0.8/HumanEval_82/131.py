
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a list comprehension to generate a list of prime numbers less than the
    # square root of the string length
    primes = [x for x in range(2, int(math.sqrt(len(string)) + 1) if not string[x] == '0' and string[x] != '1' and string[x] != '9' and string[x] != '8' and string[x] != '7']
    # If the string is not in the list, return False
    if string not in primes:
        return False
    # Return True
    return True