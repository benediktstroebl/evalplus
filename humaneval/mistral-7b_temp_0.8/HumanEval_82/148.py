
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string = list(string)
    num = 0
    for i in string:
        num += 1
    if num % 2 == 0:
        num += 1
    for i in range(1,num):
        if num % i == 0:
            return False
    return True
