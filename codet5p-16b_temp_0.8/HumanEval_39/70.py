

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

    fib_prev, fib_curr = 0, 1
    curr_number = 0
    while curr_number < n:
        curr_number += 1
        fib_prev, fib_curr = fib_curr, fib_curr + fib_prev
        is_prime = True
        for i in range(2, int(fib_curr ** 0.5) + 1):
            if fib_curr % i == 0:
                is_prime = False
                break
        if is_prime:
            continue
        else:
            break

    return fib_curr
