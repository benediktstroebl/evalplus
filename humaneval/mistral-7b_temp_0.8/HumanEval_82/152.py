
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_number = False
    for i in range(2, len(string)):
        if len(string) % i == 0:
            prime_number = True
        else:
            prime_number = False
    return prime_number
