
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    # Your code here
    if string in ['', ' ']:
        return False
    len = len(string)
    for i in range(1, len+1):
        if len % i == 0:
            if is_prime(i):
                return True
    return False
