

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
    if n < 1:
        raise ValueError("Wrong value for n")

    def is_prime(n: int):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def fibonacci(n: int):
        if n < 1:
            return None
        fib = [1, 1]
        if n == 1 or n == 2:
            return fib[n - 1]
        for i in range(2, n):
            fib.append(fib[i - 2] + fib[i - 1])
        return fib[n - 1]

    if n == 1:
        return 2

    count = 0
    for i in range(1, n + 1):
        if is_prime(fibonacci(i)):
            count += 1
            if count == n:
                return fibonacci(i)

