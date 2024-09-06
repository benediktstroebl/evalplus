def is_prime(n):
    """
    is_prime checks if a number is prime
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(13)
    True
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
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
        raise ValueError("n must be a positive integer.")
    if n <= 2:
        return 2 if n == 1 else 3
    fib_nums = [0, 1]
    for _ in range(3, n + 1):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    candidate = fib_nums[n - 1]
    while not is_prime(candidate):
        candidate = fib_nums[n - 1] = fib_nums[n - 2] + fib_nums[n - 1]
    return candidate