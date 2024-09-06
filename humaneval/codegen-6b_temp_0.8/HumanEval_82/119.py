
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) % 2 == 0:
        return False
    i = 0
    while i < len(string) / 2:
        if not string[i] == string[-1 -i]:
            return False
        i += 1
    return True    
    