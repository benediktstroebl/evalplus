
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    if string == '' or len(string) == 1:
        return True
    prime = False
    if string[0] in '0123456789':
        return False
    for i in range(len(string)):
        if i % 2 == 0:
            prime = prime or string[i] == string[i-1]
    return not prime



