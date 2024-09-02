
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # This function uses a simple trial-and-error approach
    # to determine if a number is prime.
    # If the number has more than two factors,
    # it is not considered a prime number.
    # The number 1 is not considered a prime number.
    #
    # Here is the implementation:
    for i in range(2, len(string)):
        if (string[i:i+2] == string[i:i+2] or string[i] == '1'):
            return False
    return True