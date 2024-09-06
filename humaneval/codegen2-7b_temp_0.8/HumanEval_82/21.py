
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    
    if not isinstance(string, str):
        return False
    for i in string:
        if (i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or
                i == '5' or i == '6' or i == '7' or i == '8' or i == '9'):
