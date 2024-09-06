
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    string_length = len(string)
    if string_length == 1:
        return True
    else:
        is_prime = True
        for x in range(2, string_length):
            if string_length % x == 0:
                is_prime = False
        return is_prime
