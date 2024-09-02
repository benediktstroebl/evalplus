

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
    fib_list = [0, 1]
    prime_fib_list = [2]
    while True:
        sum = fib_list[-1] + fib_list[-2]
        fib_list.append(sum)
        if is_prime(sum):
            prime_fib_list.append(sum)
            if len(prime_fib_list) == n:
                return prime_fib_list[-1]

