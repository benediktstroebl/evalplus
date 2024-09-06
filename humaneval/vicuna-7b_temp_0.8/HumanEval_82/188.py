
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) < 2:
        return False
    for i in range(2, len(string)):
        if (string[0] == string[i] or string[i-1] == string[i] or string[i-2] == string[i]) and string[i] == string[len(string)-1]:
            return False
        if string[i] == 2 or string[i] == 3 or string[i] == 4 or string[i] == 5 or string[i] == 6 or string[i] == 7 or string[i] == 8 or string[i] == 9:
            return False
    return True
