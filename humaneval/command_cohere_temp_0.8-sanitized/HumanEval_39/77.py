def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Generates the n-th Fibonacci number that is also prime.

    Args:
        n (int): The index of the required Fibonacci number.

    Returns:
        int: The n-th Fibonacci number that is also prime.
    """
    if n <= 1:
        return 2 if n == 0 else 3
    fib_nums = [0, 1]
    for i in range(2, n + 1):
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    for fib_num in fib_nums:
        if is_prime(fib_num):
            return fib_num