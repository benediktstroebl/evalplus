```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest divisor of n, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    >>> largest_divisor(20)
    10
    >>> largest_divisor(7)
    1
    """

    # Start from the number just below n and go down to 1
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return i
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(20))  # Expected output: 10
print(largest_divisor(7))   # Expected output: 1
```