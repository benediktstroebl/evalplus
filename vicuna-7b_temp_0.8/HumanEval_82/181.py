
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    for i in range(2, len(string)):
        if (string[i] == string[i-1] and string[i] != string[i-2] and string[i] % 2 == 0):
            return False
        if string[i] > 2:
            if (string[i] % 3 == 0 or string[i] % 4 == 0 or string[i] % 5 == 0 or string[i] % 6 == 0):
                return False
    return True