```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest divisor of n, smaller than n.

    Raises:
    ValueError: If n is less than or equal to 1.

    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        raise ValueError("n must be greater than 1")

    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


# Test cases
print(largest_divisor(15))  # Should print 5
print(largest_divisor(20))  # Should print 10
print(largest_divisor(30))  # Should print 15

try:
    print(largest_divisor(1))  # Should raise ValueError
except ValueError as e:
    print(e)  # Should print "n must be greater than 1"
```