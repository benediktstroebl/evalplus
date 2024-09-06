

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
    if n < 1:
        return None
    else:
        nums = [2, 3]
        for i in range(1, n):
            num = nums[-1] + nums[-2]
            for j in nums:
                if num % j == 0:
                    break
            else:
                nums.append(num)
        return nums[-1]

