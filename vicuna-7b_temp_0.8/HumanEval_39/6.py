

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
        return 2
    if n < 5:
        return 3
    fib_nums = [0, 1, 1]
    for i in range(1, n - 1):
        fib_nums.append(fib_nums[i-1] + fib_nums[i])
    for i in range(n-1, -1, -1):
        fib_nums.append(fib_nums[i-1] + fib_nums[i])
    for num in fib_nums:
        if (num > 2 and num % 2 == 0) or (num > 3 and num % 3 == 0):
            return 1
        else:
            return num
