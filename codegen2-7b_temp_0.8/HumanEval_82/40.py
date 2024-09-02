
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l < 2:
        return False
    if l == 2:
        return True
    if string[0] == '0' or string[1] == '0':
        return False
    else:
        for i in range(2, l):
            if l % i == 0:
                return False
        return
