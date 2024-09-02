
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if not string or not string.strip():
        return False
    elif not string.isnumeric():
        return False
    elif not string.isalpha():
        return False
    else:
        return string.isdigit() or string.isalpha
