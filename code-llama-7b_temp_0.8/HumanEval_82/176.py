
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Lambda function example
    def is_prime(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    # Length of string
    string_len = len(string)

    # Calling prime function
    if is_prime(string_len) == True:
        return True
    else:
        return False

