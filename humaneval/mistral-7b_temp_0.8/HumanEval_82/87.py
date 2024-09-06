
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
    string_length = int(string_length)
    if (string_length % 2 != 0):
        string_length = string_length + 1
    return is_prime(string_length)


