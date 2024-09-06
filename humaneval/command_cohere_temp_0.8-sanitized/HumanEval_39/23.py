def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Generates the n-th Fibonacci number that is also prime.

    Args:
        n (int): The index of the required Fibonacci number.

    Returns:
        int: The n-th Fibonacci number that is also a prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Start from the 3rd Fibonacci number (since the first two are 2 and 3, both prime).
        fib_num = 5
        while not is_prime(fib_num):
            # Check the next Fibonacci number (adding the last two to get the next one).
            fib_num = fib_num + fib_num[-1] + fib_num[-2]
        return fib_num