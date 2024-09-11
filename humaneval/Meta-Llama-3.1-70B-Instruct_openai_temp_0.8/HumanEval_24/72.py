```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Raises:
        ValueError: If n is less than 2.
    """
    if n < 2:
        raise ValueError("Input number should be greater than 1")

    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating from `n-1` down to `1` and checking for divisibility. The first number it finds that divides `n` evenly is the largest divisor, so it returns that number.

Note that the function raises a `ValueError` if the input `n` is less than 2, since the problem statement doesn't specify what to do in that case.