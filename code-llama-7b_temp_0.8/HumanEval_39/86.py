

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
    elif n == 2:
        return 3
    else:
        if n % 2 == 0:
            n = n + 1
        i = 3
        while True:
            fibonacci_numbers = [2, 3]
            for i in range(2, n):
                fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
            if is_prime(fibonacci_numbers[n - 1]):
                return fibonacci_numbers[n - 1]
            else:
                n = n + 2

