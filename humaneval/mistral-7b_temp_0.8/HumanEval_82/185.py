
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    string_length = len(string)
    result = 0

    for i in range(1, string_length):
        if (string_length % i) == 0:
            result += 1

    if (result == 2):
        return True
    else:
        return False
