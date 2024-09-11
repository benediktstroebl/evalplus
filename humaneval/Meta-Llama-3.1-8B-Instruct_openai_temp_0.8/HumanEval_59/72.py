### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.

    Args:
    n (int): The number to find the largest prime factor of.

    Returns:
    int: The largest prime factor of n.

    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Start checking from the largest possible factor
    for i in range(int(n**0.5) + 1, 1, -1):
        # Check if i is a factor and is prime
        if n % i == 0 and is_prime(i):
            return i

    # If no prime factors are found, return 2 (smallest prime factor)
    return 2
```
This script first checks if a number is prime by iterating from 2 to its square root. It then iterates from the square root of `n` down to 2, checking each number to see if it's a factor of `n` and if it's prime. The first such number is the largest prime factor. If no prime factors are found, the function returns 2 as it's the smallest prime factor.