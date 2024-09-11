```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and move down to 1
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
```

However, we could also use a more Pythonic approach:
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    # Use the ** operator to find the square root of n and iterate down from there
    for i in range(int(n ** 0.5), 0, -1):
        if n % i == 0:
            return n // i

# Example usage
print(largest_divisor(15))  # Output: 5
```

This version has a time complexity of O(sqrt(n)), making it more efficient for larger inputs.