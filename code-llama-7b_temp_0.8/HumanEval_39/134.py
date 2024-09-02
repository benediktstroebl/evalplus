

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
    k = 0
    fib_list = [2, 3]
    while len(fib_list) < n + 1:
        last = fib_list[-1]
        next_fib = last + fib_list[-2]
        if is_prime(next_fib):
            fib_list.append(next_fib)
        else:
            k += 1
    return fib_list[n]

