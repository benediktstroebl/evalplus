
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    prime_length = 0
    for letter in string:
        prime_length += 1
    if prime_length == 2:
        return True
    elif prime_length % 2 == 0:
        return False
    else:
        for i in range(2, prime_length):
            if prime_length % i == 0:
                return False
        return True


