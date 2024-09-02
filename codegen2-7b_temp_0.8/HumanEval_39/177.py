

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
    if n <= 2:
        return 2
    else:
        fibonacci_list = [2, 3]
        while fibonacci_list[0] < n:
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
        return fibonacci_list[n-1
