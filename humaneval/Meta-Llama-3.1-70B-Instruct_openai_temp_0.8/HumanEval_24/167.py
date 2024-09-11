```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Raises:
        ValueError: If n is less than 1.

    Examples:
        >>> largest_divisor(15)
        5
    """

    # Check if n is less than 1
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")

    # Start checking from n - 1
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as it's the largest divisor
            return i

    # If no divisor is found, return 1 (since 1 is a divisor of every number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```