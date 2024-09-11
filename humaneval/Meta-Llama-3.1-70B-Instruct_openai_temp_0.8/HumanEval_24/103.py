```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(17)
        1
    """
    # Iterate from n-1 down to 1 (inclusive) to find the largest divisor
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i


# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n-1` down to 1 and checks each number to see if it is a divisor of `n`. As soon as it finds a divisor, it returns that number as the largest divisor.