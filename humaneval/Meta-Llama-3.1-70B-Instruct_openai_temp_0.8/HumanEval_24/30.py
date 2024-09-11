```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number for which to find the largest divisor.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Raises:
        ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("Input number should be greater than 0")

    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(25))  # Output: 5
print(largest_divisor(17))  # Output: 1
```