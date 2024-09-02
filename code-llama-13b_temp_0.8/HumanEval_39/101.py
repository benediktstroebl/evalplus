

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
    if n <= 0:
        return -1

    f_1 = 0
    f_2 = 1
    f_n = f_1 + f_2

    cnt = 0
    while True:
        cnt += 1

        f_1 = f_2
        f_2 = f_n
        f_n = f_1 + f_2

        is_prime = True
        for i in range(2, int(f_n**0.5) + 1):
            if f_n % i == 0:
                is_prime = False
                break

        if is_prime:
            if cnt == n:
                return f_n

    return -1

