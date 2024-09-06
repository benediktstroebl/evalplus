
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # create dictionary with values as booleans for each prime number
    primes = {2:True, 3:True, 5:True, 7:True, 11:True, 13:True, 17:True, 19:True, 23:True, 29:True, 31:True,
             37:True, 41:True, 43:True, 47:True, 53:True, 59:True, 61:True, 67:True, 71:True, 73:True, 79:True,
             83:True, 89:True, 97:True, 101:True}
    # get length of string
    string_len = len(string)
    # loop through dictionary
    for prime in primes:
        # if prime number matches string length, return True
        if prime == string_len:
            return True
        # if prime number is greater than string length, break
        elif prime > string_len:
            break
    # if none of the primes match, return False
    return False
