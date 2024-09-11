```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n smaller than n.

    Example:
    >>> largest_divisor(15)
    5
    """
    # Start from n - 1, since the problem statement specifies the divisor should be smaller than n
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it immediately, since we're iterating in descending order
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(30))  # Output: 15
```