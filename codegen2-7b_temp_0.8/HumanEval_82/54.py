
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    return string == ''.join(list(filter(lambda x: int(x) > 1, map(str, range(2, int(len(string) + 1))))
