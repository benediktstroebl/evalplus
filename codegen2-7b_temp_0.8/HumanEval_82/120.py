
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    len(string)
    if string.isalpha():
        return False
    if len(string) == 2:
        return True
    for i in string:
        if i == " ":
            return False
        for j in range(2, int(i)):
            if i % j == 0:
                return False
    return
