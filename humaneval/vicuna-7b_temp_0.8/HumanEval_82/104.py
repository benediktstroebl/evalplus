
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def is_prime(n, max_value):
        """Check if a number is prime
        """
        if n == 2:
            return True
        elif n % 2 == 0:
            return False
        elif n <= max_value:
            return False
        else:
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

    max_value = int(len(string)**0.5)
    for char in string:
        if char.isalpha():
            max_value += 1
    if max_value == string.count(' '):
        return True
    for i in range(1, int(max_value**0.5) + 1):
        if string.count(str(i)) % (i + 1) == 0:
            return False
    return True