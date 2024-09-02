
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
    if string[0] != "1" or string[-1] != "1":
        return False
    l = len(string)
    for i in range(2, l//2 + 1):
        count = 0
        for j in range(1, l):
            if string[j] == string[j-i]:
                count += 1
        if count > 1:
            return False
    return True

