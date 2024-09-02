
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
    for i in string:
        if i == " ":
            continue
        i = ord(i) - ord('a') + 1
        if i < 2:
            return False
        for j in range(2, i):
            if i % j == 0:
                return False
    return True
