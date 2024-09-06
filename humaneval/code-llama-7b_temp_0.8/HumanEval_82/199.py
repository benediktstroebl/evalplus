
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # pass
    # test if the string length is a prime number
    # If it is a prime number, return True
    # If it is not a prime number, return False
    # HINT: len(string) will return the length of the string
    # HINT: prime numbers are numbers that can't be evenly divided by any
    # number other than 1 and the number itself.
    # 1 is not prime
    # 2 is prime
    # 3 is prime
    # 4 is not prime
    # 5 is prime
    # 6 is not prime
    # 7 is prime
    # 8 is not prime
    # 9 is not prime
    # 10 is not prime
    # 11 is prime
    # 12 is not prime
    # 13 is prime
    # 14 is not prime
    # 15 is not prime
    # 16 is not prime
    # 17 is prime
    # 18 is not prime
    # 19 is prime
    # 20 is not prime
    if len(string) == 2 or len(string) == 3:
        return True
    elif len(string) == 5 or len(string) == 7:
        return True
    elif len(string) > 2 and len(string) < 8:
        return False
    else:
        for i in range(2, len(string)):
            if len(string) % i == 0:
                return False
        return True
