

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
    curr_num = 1
    next_num = 1
    fib_nums = []
    fib_nums.append(1)
    fib_nums.append(1)
    for _ in range(n - 2):
        curr_num, next_num = next_num, curr_num + next_num
        fib_nums.append(next_num)
    return fib_nums[n - 1]

