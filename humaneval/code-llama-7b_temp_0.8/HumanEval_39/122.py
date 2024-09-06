

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
    nums = [2, 3]
    if n <= 1:
        return nums[n]
    else:
        i = 3
        while len(nums) < n:
            if is_prime(i):
                fib = fibonacci(i)
                if fib and is_prime(fib):
                    nums.append(fib)
            i += 1
        return nums[-1]

