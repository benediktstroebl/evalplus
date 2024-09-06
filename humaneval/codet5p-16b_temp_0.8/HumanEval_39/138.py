

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
    numbers = [1, 1]
    i = 2
    while i < n:
        numbers.append(numbers[i - 2] + numbers[i - 1])
        if is_prime(numbers[i]):
            i += 1
    return numbers[n - 1]

