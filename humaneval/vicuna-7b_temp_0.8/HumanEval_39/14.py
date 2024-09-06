

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
    fibonacci_series = []
    for i in range(1, n):
        fibonacci_series.append(fibonacci(i))
    result = []
    for i in range(1, n):
        if fibonacci_series[i] % 2 == 0:
            break
    result.append(fibonacci_series[i])
    for i in range(2, n):
        if fibonacci_series[i] % 2 == 0:
            result.append(0)
        else:
            result.append(fibonacci_series[i])
    for i in result:
        if i % 2 != 0:
            return i
    return 0
