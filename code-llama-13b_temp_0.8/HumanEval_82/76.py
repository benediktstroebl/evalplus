
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return False
    if len(string) in [2, 3, 5, 7]:
        return True
    if len(string) > 1:
        for i in range(2, len(string)):
            if not (len(string) % i):
                return False
        return True
    return False

