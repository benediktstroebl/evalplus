```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.

    Raises:
    ValueError: If n is less than 2, since there are no divisors smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    >>> largest_divisor(17)
    1
    """

    if n < 2:
        raise ValueError("Input number should be greater than 1")

    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
```