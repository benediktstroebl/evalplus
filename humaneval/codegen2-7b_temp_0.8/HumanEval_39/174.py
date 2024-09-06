

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
    nums = [0, 1]
    for i in range(2, n):
        nums.append(nums[i-1] + nums[i-2])
    return nums[n-1] if is_prime(nums[n-1]) else
