

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
    if n == 0 or n == 1:
        return n

    # First check if n-1 or n-2 is a Fibonacci number, if it is, then it is prime.
    # Return 2^n because a prime number is greater than 2^n
    # (e.g. 2^2 = 4 is a Fibonacci number, so the prime factorization is 2*2^2)
    if n % 2 == 0:
        if is_fib(n-2):
            return 2
    if n % 2 == 1:
        if is_fib(n-1):
            return 2

    # Otherwise, if n-1 or n-2 is not a Fibonacci number, then n-1 or n-2 is prime
    # Go to the beginning of the algorithm and check if n-1 or n-2 is prime, then return
    # the result. Then, recursively call the function until n is less than 2, in which
    # case the algorithm will return 2 as the result.
    x = math.sqrt(n)
    greater = int(x) + 1
    while n % greater != 0:
        greater += 1
    if greater % 2 == 0:
        return greater

    return n

