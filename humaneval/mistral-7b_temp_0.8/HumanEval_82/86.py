
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # your code here
    if len(string) == 1 or len(string) == 2:
        return True
    elif len(string) % 2 == 0:
        return False
    for i in range(3, len(string), 2):
        if len(string) % i == 0:
            return False
    return True
