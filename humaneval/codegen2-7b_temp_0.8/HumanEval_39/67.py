

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
    nums = [1, 2]
    i = 2
    while len(nums) < n:
        fib_num = nums[-2] + nums[-1]
        is_prime = True
        for num in nums:
            if num > fib_num:
                is_prime = False
        if is_prime:
            nums.append(fib_num)
        i += 1
    return num
