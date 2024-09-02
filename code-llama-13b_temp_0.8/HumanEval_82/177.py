
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
        if n % 2 == 0 and n != 2:
            return False
        return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))
    return is_prime(len(string))

    # return is_prime(len(string))

