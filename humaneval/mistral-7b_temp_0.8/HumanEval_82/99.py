
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string = string.replace(" ","")
    n = len(string)
    c = 2
    for i in range(2, n):
        if n % c == 0:
            return False
        else:
            c += 1
    return True
