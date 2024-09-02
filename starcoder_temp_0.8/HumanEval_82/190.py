
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if not string:
        return False
    else:
        for num in range(2, len(string) + 1):
            if len(string) % num == 0:
                return False
        return True
