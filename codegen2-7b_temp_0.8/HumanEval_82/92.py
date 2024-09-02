
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if string[0].isdigit():
        return False
    for i in range(2, int(math.sqrt(len(string))) + 1):
        if string[0] % i == 0:
            return False
    return
