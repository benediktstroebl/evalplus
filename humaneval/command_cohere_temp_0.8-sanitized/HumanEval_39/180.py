def is_prime(n):
    """
    Checks if a number is prime
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
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be a positive integer.")
    if n == 1:
        return 2
    if n == 2:
        return 3
    fib_nums = [0, 1]
    for i in range(2, n + 1):
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    for _ in range(n - 2):
        if not is_prime(fib_nums[_]):
            continue
        return fib_nums[_]
    return fib_nums[n - 1]