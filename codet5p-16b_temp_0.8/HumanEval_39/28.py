

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
    i = 2
    while True:
        i += 1
        if i % 2 == 1:
            fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
        else:
            fib_nums.append(fib_nums[i-1] + fib_nums[i-2] + 1)
        if all(is_prime(k) for k in fib_nums[-i:]) and len(fib_nums) >= n:
            return fib_nums[-i]

