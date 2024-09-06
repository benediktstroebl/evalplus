

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

    def is_prime(num: int):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    fib_nums = [1, 1]

    while len(fib_nums) < n:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])

    for i in range(len(fib_nums) - 1, -1, -1):
        if is_prime(fib_nums[i]):
            return fib_nums[i]
