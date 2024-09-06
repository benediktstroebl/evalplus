

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
    fib_list = [2, 3]
    prime = [2, 3]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
        # print(fib_list)
        if is_prime(fib_list[-1]):
            prime.append(fib_list[-1])

    return prime[-1]

