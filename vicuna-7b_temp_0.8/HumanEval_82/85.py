
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
    def is_prime(n, p_start=2, p_end=1000000):
        for p in range(p_start, p_end+1):
            if n % p == 0:
                return False
        return True

    for char in string:
        if char.isalpha():
            if is_prime(int(string)):
                return True
        else:
            if is_prime(int(string)):
                return True

    return False
