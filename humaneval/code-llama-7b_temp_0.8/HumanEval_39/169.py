

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
    # Performs a binary search to find the nth prime fibonacci number
    # Time complexity: O(log(n))
    if n == 1:
        return 2
    if n == 2:
        return 3

    # Initialize low and high variables
    low = 0
    high = 1000000000

    # Keep decrementing high until the condition is satisfied
    while high - low > 1:
        mid = (high + low) // 2
        # Check if mid is the solution
        if is_fib(mid) and is_prime(mid):
            return mid
        # Otherwise shrink the search space
        if is_fib(mid):
            high = mid
        else:
            low = mid

