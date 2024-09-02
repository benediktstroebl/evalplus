

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
    elif n < 4:
        return 2
    else:
        prime_nums = [2, 3]
        i = 1
        while len(prime_nums) <= n:
            prime_nums.append(prime_nums[i-1] + prime_nums[i] - 1)
            i += 1
        return prime_nums[n]

