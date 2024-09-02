
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Define the sieve of Eratosthenes
    sieve = [True] * (1000000 // 2)
    for i in range(1000001, 0, -1):
        sieve[i] = (i % 2 == 0)
    for i in range(2, len(string)):
        for j in range(i, len(string)):
            if (string[i:j] == string[i] or string[i:j] == string[j]) and sieve[j] == True:
                sieve[i:j] = False
                break
    return len(string) == 2 or len(string) % 2 == 0
