

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
    elif n == 2:
        return 3

    cnt = 2
    fib_num = [2, 3]
    fib_set = set([2, 3])

    while cnt < n:
        fib_num.append(fib_num[cnt - 1] + fib_num[cnt - 2])
        if is_prime(fib_num[cnt]):
            fib_set.add(fib_num[cnt])
            cnt += 1
        else:
            fib_num.pop()

    return fib_set.pop()

