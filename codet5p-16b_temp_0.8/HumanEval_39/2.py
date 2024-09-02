

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

    import math
    primes = []

    def is_prime(n: int) -> bool:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def prime_list(n: int) -> list:
        prime_list = []
        for i in range(2, n + 1):
            if is_prime(i):
                prime_list.append(i)
        return prime_list

    def prime_fib(n: int) -> int:
        i = 2
        while True:
            if is_prime(i) and Fibonacci(i) <= n:
                primes.append(i)
                i += 1
            else:
                return primes[-1]

    return prime_fib(n)

