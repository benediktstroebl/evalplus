
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # your code here
    def is_prime(n):
        # check if n is prime
        if n == 2:
            return True
        elif n == 3:
            return True
        elif n % 2 == 0:
            return False
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

    for char in string:
        if is_prime(ord(char)):
            return True
    return False
