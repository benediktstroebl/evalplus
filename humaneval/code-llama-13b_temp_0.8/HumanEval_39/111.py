

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
    fib = [0, 1]
    index = 2
    # Generate Fibonacci series
    while fib[index] <= n:
        fib.append(fib[index - 2] + fib[index - 1])
        index += 1

    # Find the first prime in the Fibonacci series
    i = 1
    while i < len(fib):
        if is_prime(fib[i]):
            return fib[i]
        i += 1

