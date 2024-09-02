

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
    p_list = [2]
    f_list = [0, 1]
    i = 2
    while True:
        f_list.append(f_list[i - 1] + f_list[i - 2])
        if is_prime(f_list[i]):
            p_list.append(f_list[i])
            i += 1
            if i == n:
                return f_list[i]
        else:
            i += 1

