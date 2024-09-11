```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Raises:
        ValueError: If n is less than 2.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(12)
        6
        >>> largest_divisor(2)
        1
    """
    if n < 2:
        raise ValueError("Input number should be greater than or equal to 2")

    # Start checking divisors from the largest possible number (n-1) down to 1
    for i in range(n-1, 0, -1):
        # Check if current number i divides n evenly
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
print(largest_divisor(2))   # Output: 1
```