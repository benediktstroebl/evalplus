

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
    fib_nums = [2, 3]
    while len(fib_nums) < n:
        next_num = fib_nums[-1] + fib_nums[-2]
        if is_prime(next_num):
            fib_nums.append(next_num)
    return fib_nums[n - 1]
