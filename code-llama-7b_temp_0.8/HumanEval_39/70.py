

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
    primes = [2]
    while len(primes) <= n:
        fib_num = sum(fib_nums)
        fib_nums.append(fib_num - fib_nums[-1])
        if is_prime(fib_num):
            primes.append(fib_num)

    return primes[n]

