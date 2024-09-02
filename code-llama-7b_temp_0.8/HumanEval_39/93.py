

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
    fib_nums = [1, 1]

    while len(fib_nums) < n:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])

    for i in fib_nums[-3:]:
        if i < n:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            return i

