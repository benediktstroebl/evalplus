### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(12))  # Output: 6
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest divisor of `n` that is smaller than `n`. The function uses a simple loop to iterate from `n-1` down to `1` and checks if each number is a divisor of `n`. The first divisor found is returned as the result.