
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 1:
        return True
    if l == 2:
        return (string[0] != string[1])
    for i in range(2, l):
        if (string[0] == string[i]) or (string[-i] == string[-i]):
            return False
        if l % i == 0:
            return False
    return True

