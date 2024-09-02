

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
    first = 0
    second = 1
    is_prime = True
    while True:
        if first % 2 == 0:
            first = second
            second = first + second
        else:
            second = first + second
            first = second
        if first == 1:
            first = second
            second = first + second
        is_prime = True
        for i in range(2, int(second ** 0.5) + 1):
            if second % i == 0:
                is_prime = False
                break
        if is_prime:
            return second
        first = second
        second = first + second

