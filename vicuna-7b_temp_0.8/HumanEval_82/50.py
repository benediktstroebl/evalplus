
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
        """Check if a number is prime
        """
        if n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
    
    for char in string:
        if char.isalpha() or char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9':
            n = int(string)
            while n > 1:
                if is_prime(n):
                    return True
                n = n - 2
        else:
            return False
    return False
