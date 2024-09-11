```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Raises:
        ValueError: If n is less than or equal to 1.

    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(20)
        10
    """
    if n <= 1:
        raise ValueError("Input number should be greater than 1")

    # Start from the largest possible divisor, which is n // 2
    for i in range(n // 2, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(20))  # Expected output: 10
```