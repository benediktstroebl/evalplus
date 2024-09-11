```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.
    """
    # Start checking from the largest possible divisor, which is n // 2
    for i in range(n // 2, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script starts checking for divisors from the largest possible number (`n // 2`) and goes down to 1. As soon as it finds a number that divides `n` evenly (i.e., `n % i == 0`), it returns that number as the largest divisor.

Alternatively, you could use a more mathematical approach to solve this problem. Since the largest divisor of a number is the number itself divided by its smallest prime factor, we can use the following code:

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.
    """
    def smallest_prime_factor(x: int) -> int:
        """Find the smallest prime factor of x"""
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return i
        return x

    # Return n divided by its smallest prime factor
    return n // smallest_prime_factor(n)

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This code uses a helper function `smallest_prime_factor` to find the smallest prime factor of `n`, and then divides `n` by this factor to get the largest divisor.