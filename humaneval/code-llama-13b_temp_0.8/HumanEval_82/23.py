
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # return len(string) in [2, 3, 5, 7]
    # return len(string) > 1 and all(len(string) % i for i in range(2, len(string)))
    return len(string) > 1 and all(string % i for i in range(2, len(string)))
