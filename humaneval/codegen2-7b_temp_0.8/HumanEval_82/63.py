
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_check = True
    for i in range(2, len(string)):
        if string[i] == string[i-1]:
            prime_check = False
    return prime_check
