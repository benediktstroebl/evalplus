
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return False
    string_int = 0
    for letter in string:
        string_int += ord(letter) - 96
    if string_int % 2 == 0:
        return False
    return True
