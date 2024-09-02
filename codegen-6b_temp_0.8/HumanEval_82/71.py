
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        else:
            i = 2
            while i < n:
                if n % i == 0:
                    return False
                i += 1
            return True
    length = len(string)
    if length == 1:
        return True
    else:
        i = 2
        while i < length:
            if is_prime(i) == True:
                if string[:i] * (length // i) == string:
                    return True
            i += 1
        return False
