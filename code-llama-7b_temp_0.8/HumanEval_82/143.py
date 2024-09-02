
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    return len(string) == 0 or len(string) == 1 or len(string) == 2 or prime_length(string[1:]) and len(string) % 2 == 1
