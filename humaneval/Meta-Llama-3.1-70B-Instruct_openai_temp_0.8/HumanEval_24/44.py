```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n that is smaller than n.

    >>> largest_divisor(15)
    5
    """
    # Start from n-1 and decrease by 1 in each iteration
    for i in range(n-1, 0, -1):
        # Check if the current number divides n evenly
        if n % i == 0:
            # If it does, return it as the largest divisor
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(30))  # Output: 15
```