
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    return len(string) in [2,3] or [x for x in range(2, int(len(string)**0.5)+1) if string.count(string[:x]) == 1] == []
