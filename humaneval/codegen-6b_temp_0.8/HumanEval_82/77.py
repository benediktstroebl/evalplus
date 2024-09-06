
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) < 3:
        return True

    if len(string) == 3:
        return True if string[0] == string[1] == string[2] else False
    
    return prime_length(string[1:]) if string[0] == string[-1] else False

