
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check for empty string
    if not string:
        return False
    
    # Check for prime number
    for num in range(2, int(string[0] * 10) + 1):
        if string[0] == '1' or string[0] == '3' or string[0] == '7' or string[0] == '9':
            if string[1:] % num == 0:
                return False
        else:
            if string[1:] % num == 0:
                return False
    return True
