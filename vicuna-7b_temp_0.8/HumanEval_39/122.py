

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
    if n < 2 or n > 42:
        return 0

    fibonacci_numbers = [2, 1]

    for i in range(n):
        fibonacci_numbers.append(fibonacci_numbers[-2] + fibonacci_numbers[-1])

    for prime in primes:
        if prime not in fibonacci_numbers:
            return prime

    return 0
