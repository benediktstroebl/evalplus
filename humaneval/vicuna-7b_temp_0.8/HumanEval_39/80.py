

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
    # Checking if n is prime
    if not n % 1:
        raise ValueError("n must be prime")

    # Checking if n is a Fibonacci number
    if n <= 1:
        return 2
    elif n <= 2:
        return 3
    else:
        fib = [2, 1]
        result = 2
        for i in range(3, n, 2):
            fib.append(fib[-1] + fib[-2])
        result = fib[-1]
        while result % 2 != 1:
            result = (result * result) % n
        return result
