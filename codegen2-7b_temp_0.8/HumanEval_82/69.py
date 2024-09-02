
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    return string.lower().count('on') == 1 and string.lower().count('at') == 1 and string.lower().count('or') == 1 and string.lower().count('in') == 1 and string.lower().count('by') ==
