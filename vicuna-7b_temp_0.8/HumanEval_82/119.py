
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your code here
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    string_chars = set(string)
    prime_length = [0] * len(string_chars)
    for i in range(1, len(string_chars)):
        if is_prime(int(string_chars[i])):
            prime_length[i] = int(string_chars[i])
    for i in range(1, len(prime_length)):
        if prime_length[i] < prime_length[i-1] * 2:
            return False
    return True
