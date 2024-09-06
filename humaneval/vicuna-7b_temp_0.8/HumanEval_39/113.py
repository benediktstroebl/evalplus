

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # Check that n is greater than 1
    if n < 2:
        return 2

    # Check if the number is prime
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    # Use the Sieve of Eratosthenes algorithm to check if the number is prime
    # We use a list to store the prime numbers
    prime_list = [True for i in range(2, n + 1)]
    for i in range(2, int(n**0.5) + 1):
        if i not in prime_list:
            prime_list[i] = False
    for p in prime_list:
        if n % p == 0:
            return 2

    # If the number is not prime, return 2
    return 2
