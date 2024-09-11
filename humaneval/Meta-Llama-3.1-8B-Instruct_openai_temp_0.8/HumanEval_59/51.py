```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.

    Args:
    n (int): The input number.

    Returns:
    int: The largest prime factor of n.

    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    def is_prime(x: int) -> bool:
        """
        Check if x is a prime number.

        Args:
        x (int): The number to check.

        Returns:
        bool: True if x is prime, False otherwise.
        """
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    for i in range(n, 1, -1):
        # Check if i is a factor of n and is prime
        if n % i == 0 and is_prime(i):
            return i
```

This script uses a helper function `is_prime` to check if a number is prime. It starts checking from the number itself down to 2 and returns the first factor that is also a prime number. 

Note that we only need to check up to the square root of `n` to determine if it's prime, which is why we use `int(x ** 0.5) + 1` in the `is_prime` function. This is a common optimization when checking for prime numbers. 

Also, this script assumes that `n` is a positive integer greater than 1, as per the problem statement. If `n` can be negative or 1, additional checks will be needed.