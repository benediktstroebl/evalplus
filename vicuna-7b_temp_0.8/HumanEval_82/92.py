
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Check if the string is empty or not
    if not string:
        return False

    # Check if the string is a prime number or not
    # Here we are using Sieve of Eratosthenes algorithm
    sieve = [True] * (int(math.sqrt(len(string)) + 1) ** 2)
    for i in range(2, len(string)):
        if sieve[i]:
            for j in range(i ** 2, len(string), i):
                sieve[j] = False
    return len(string) > 2 and all(sieve[i] for i in range(len(string)))
