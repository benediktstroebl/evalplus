
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
        """Return True if n is prime, otherwise return False
        """
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for char in string:
        if char.isdigit():
            for i in range(int(string[0])**2, len(string)+1):
                if string[i:i+2] == str(int(string[i])**2):
                    return False
    return True
