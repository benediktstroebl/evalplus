

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
    fib_num = 1
    fib_num2 = 2
    is_prime = True

    while fib_num < n:
        fib_num2, fib_num = fib_num, fib_num2 + fib_num
        if fib_num2 > n:
            break

        for i in range(2, fib_num2):
            if fib_num2 % i == 0:
                is_prime = False
                break

        if is_prime:
            return fib_num2

    return fib_num2

