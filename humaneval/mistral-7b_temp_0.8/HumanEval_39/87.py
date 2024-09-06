

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
    fib_numbers = [2, 3]
    prime_numbers = [2, 3]
    while len(prime_numbers) < n:
        fib = fib_numbers[-1] + fib_numbers[-2]
        if all(fib % i != 0 for i in prime_numbers):
            prime_numbers.append(fib)
            fib_numbers.append(fib)
    return fib_numbers[n-1]

