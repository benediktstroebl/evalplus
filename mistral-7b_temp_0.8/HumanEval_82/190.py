
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    result = True
    string = string.lower()
    string_length = len(string)
    i = 2
    while i < string_length:
        if string_length % i == 0:
            result = False
            break
        i += 1
    return result
