
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    return len(string) == 1 or string[0] =='' or all(c.isalpha() for c in string) or string[-1] =='' or any(c.isdigit() for c in string[1:-1
