
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) == 1:
        return False
    if len(string) == 2:
        return True
    if len(string) % 2 != 0:
        return False
    half = len(string) / 2
    for i in range(0, half):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

