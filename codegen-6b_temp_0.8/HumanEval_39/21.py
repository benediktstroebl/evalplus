

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
    if n < 2:
        return 1
    if n == 2 or n == 3:
        return 2
    fib_list = [1, 1]
    cnt = 3
    while cnt < n:
        fib_list.append(fib_list[cnt - 1] + fib_list[cnt - 2])
        cnt += 1

    fib_list = fib_list[:-1]
    # The last element is a Fibonacci, so we remove it.
    # The first element is a Fibonacci, so we remove it.
    i = 0
    while i < len(fib_list):
        if is_prime(fib_list[i]):
            i += 1
        else:
            fib_list.pop(i)
    return fib_list[-1]

