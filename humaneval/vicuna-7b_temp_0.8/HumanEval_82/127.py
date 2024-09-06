
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
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for char in string:
        if char == '1' or char == '3' or char == '7' or char == '9':
            continue
        for i in range(2, int(string**0.5) + 1):
            if string[i:i+2] in ['11', '121111']:
                return False
        if is_prime(int(string)) == False:
            return False
    return True
