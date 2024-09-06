

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

    primes = [2]
    fib_nums = [1, 1]
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        for i in range(3, n + 1):
            while not is_prime(fib_nums[i - 1] + fib_nums[i - 2]):
                fib_nums[i - 1] += fib_nums[i - 2]
            primes.append(fib_nums[i - 1])
        return primes[-1]

