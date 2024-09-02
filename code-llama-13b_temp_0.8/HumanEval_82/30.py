
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def prime(n):
        if n < 2:
            return False
        if n == 2 or n == 3 or n == 5:
            return True
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            return False
        for i in range(6, int(n ** 0.5) + 1, 6):
            if n % (i + 1) == 0 or n % (i + 4) == 0:
                return False
        return True

    return prime(len(string))

