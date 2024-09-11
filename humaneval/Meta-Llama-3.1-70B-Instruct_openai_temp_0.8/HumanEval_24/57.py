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
        >>> largest_divisor(100)
        50
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(100))  # Output: 50
```
This script defines the `largest_divisor` function, which iterates over numbers from `n-1` down to 1 to find the largest number that divides `n` evenly. The function returns the first divisor it finds, which will be the largest due to the reverse iteration order.