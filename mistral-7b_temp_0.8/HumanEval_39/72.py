

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
    n = int(n)
    prime_fib_list = [2, 3, 5, 13, 89]
    for i in range(6, n):
        fib_num = fib_of_n(i)
        if fib_num == 1:
            continue
        if is_prime(fib_num):
            prime_fib_list.append(fib_num)
    return prime_fib_list[n-1]
