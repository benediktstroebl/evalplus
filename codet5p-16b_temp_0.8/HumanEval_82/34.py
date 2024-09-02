
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    string = string.lower()
    num = 0
    for c in string:
        if c.isalpha():
            num += 1
    if num == 0:
        return False
    if num == 1:
        return True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
