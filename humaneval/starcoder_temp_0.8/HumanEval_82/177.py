
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    import math
    if string == '':
        return False
    length = len(string)
    #or math.sqrt(length) == int(math.sqrt(length))
    if length % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(length))+1, 2):
        if length % x == 0:
            return False
    return True
