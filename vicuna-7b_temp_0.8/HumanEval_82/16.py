
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
        """Returns True if n is prime, False otherwise"""
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, len(string)):
        if string[i] == string[0] and string[i] not in string[0]:
            return True
        if is_prime(int(string[i])):
            return True
    return False