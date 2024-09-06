
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use Sieve of Eratosthenes algorithm to check if a number is prime
    sieve = [True] * (int(math.sqrt(x) + 1) // 2)
    for i in range(2, int(math.sqrt(len(string) + 1)) + 1):
        if string[i:i+2] in sieve:
            sieve[string[i:i+2]] = False
    return len(string) in sieve
