
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    #return len(string) in set(filter(lambda x: bool(x), [i for i in range(1, len(string)+1, 2)]))
    return len(string) in [i for i in range(2, len(string)+1) if not len(string)%i]

