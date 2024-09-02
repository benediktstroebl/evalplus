
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # your code to implement the function goes here
    # you can use the Sieve of Eratosthenes algorithm or use a list and check if the number is divisible by any of the previous numbers
    # you can also use a boolean array
    # make sure to check the length of the string and return True or False accordingly

    # Example of using Sieve of Eratosthenes
    def sieve(n):
        # Create a boolean array with the values True for prime numbers and False for composite numbers
        prime = [True for i in range(1, n + 1)]
        composite = [False for i in range(1, n + 1)]
        while len(prime) < n:
            p = 2
            while p * p <= n:
                if p in prime:
                    for i in range(p * p, n + 1, p):
                        prime[i] = False
                        composite[i] = True
        return prime

    # check if the string length is prime
    string_length = len(string)
    prime = sieve(string_length)
    for i in range(2, string_length + 1):
        if prime[i]:
            return True
    return False
