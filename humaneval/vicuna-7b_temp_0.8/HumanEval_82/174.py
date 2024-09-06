
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def is_prime(n, max_val):
        if n < 2:
            return False
        for i in range(2, int(max_val ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_count = 0
    for i in range(1, len(string)):
        if is_prime(string[0], string[0]):
            prime_count += 1
    if prime_count == len(string) - 1:
        return True
    return False
