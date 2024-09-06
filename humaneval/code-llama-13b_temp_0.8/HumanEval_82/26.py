
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    s = set(range(2, len(string)+1))
    for i in range(2, len(string)):
        s = s - set(range(2*i, len(string)+1, i))
    return len(string) in s

