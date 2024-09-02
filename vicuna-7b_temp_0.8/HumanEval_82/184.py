
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a helper function to check if the string is prime
    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        elif n % 2 != 0:
            return False
        else:
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
    
    # Use the helper function to check if the string is prime
    for i in range(1, len(string) + 1):
        if is_prime(string[i:]) == False:
            return False
    return True
