
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
        """
        return True if n is prime, False otherwise
        """
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    string_chars = string.lower()
    prime_list = [i for i in range(2, int(len(string_chars) ** 0.5) + 1) if string_chars[0] == i or string_chars[0] == i + 1]
    for i in prime_list:
        for j in range(1, len(string_chars)):
            if string_chars[j] == i:
                return False
    return True
