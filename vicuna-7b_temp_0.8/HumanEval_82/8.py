
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
    n = len(string)
    for i in range(2, n):
        if (string[i:i+2) == string[i:i+2]):
            return False
        if (string[i:i+2) not in string[i:i+2]):
            return False
    return True
