
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    def check_prime(string):
        length = len(string)
        if length == 1:
            return False
        else:
            for i in range(1, length+1):
                if length % i == 0 and i != length:
                    return False
                elif length % i == 0 and i == length:
                    return True

    return check_prime(string)

