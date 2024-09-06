
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check if the string length is less than 2
    if len(string) < 2:
        return True

    # Check if the string length is prime
    for i in range(2, len(string)):
        if (string[0] == string[i]) and (string[0] == string[i+1]):
            return False
        if (string[0] != string[i]) and (string[i] % 2 == 0 and string[i] % 3 == 0):
            return False
        if (string[i-1] == string[i]) and (string[i-1] == string[i+1]):
            return False
        if (string[i-1] != string[i]) and (string[i] % 2 == 0 and string[i] % 3 == 0):
            return False

    return True
