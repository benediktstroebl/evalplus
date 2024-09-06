

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
    # Checking that n is a positive integer
    if n < 1:
        raise ValueError("Value of n must be positive integer!")
    # Checking that n is prime and generates fibonacci sequence
    if n < 4 and is_prime(n):
        return n
    if n % 2 == 0 or n % 3 == 0:
        raise ValueError("Value of n must be prime and must be greater than 3!")
    else:
        sieve = [True] * (n+1)
        mroot = int(n**0.5)
        for x in range(1, mroot+1):
            if sieve[x]:
                for i in range(x*x, n+1, x*2):
                    sieve[i] = False
        # Fibonacci number is the sum of all prime numbers
        fib = 1
        start = 3
        while start <= n:
            if sieve[start] == True:
                fib += start
                start += 2
            else:
                start += 2
        return fib

