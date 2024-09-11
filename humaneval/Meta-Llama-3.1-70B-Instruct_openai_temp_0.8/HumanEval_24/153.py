```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(35))  # Output: 7
```

This script defines a function `largest_divisor` that iterates over the numbers from `n-1` down to 1. It checks for each number whether it is a divisor of `n` by checking the remainder of `n` divided by the number. The first number for which the remainder is 0 is the largest divisor of `n` smaller than `n`, so the function immediately returns this number.

Note that this function will return the correct result for any positive integer `n`, but it may be inefficient for large numbers due to its trial division approach. If performance is a concern, you may want to consider more advanced algorithms or data structures for finding divisors, such as prime factorization or a divisor sieve.