
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check for prime numbers
    for i in range(2, len(string) + 1):
        if string[i:i+2] == string[i:i+2] % 2 == 1:
            return True
    return False
