
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
        """Return True if n is prime, False otherwise"""
        if n < 2:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
    
    for char in string:
        if char.isalpha() and char.islower():
            string = string.replace(char, '_')
    
    n = int(string)
    for i in range(1, n+1):
        if is_prime(i) or n % i == 0:
            return False
    return True
