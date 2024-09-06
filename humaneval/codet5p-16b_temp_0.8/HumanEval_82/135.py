
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if (string.count('a') + string.count('A') + string.count('e') + string.count('E') + string.count('i') + string.count('I') + string.count('o') + string.count('O') + string.count('u') + string.count('U')) == 0:
        return (len(string) == 2 or len(string) == 3)
    else:
        return False
    
