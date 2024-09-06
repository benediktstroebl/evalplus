

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
    if n == 1:
        return 2

    if n == 2:
        return 3

    def is_prime(num: int):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    current = 1
    fib_array = [2, 3]
    for i in range(2, n):
        current = fib_array[-1] + fib_array[-2]
        fib_array.append(current)

    while not is_prime(current):
        current = fib_array[-1] + fib_array[-2]
        fib_array.append(current)

    return current

