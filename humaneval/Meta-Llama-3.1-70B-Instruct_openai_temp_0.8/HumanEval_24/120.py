```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The number for which to find the largest divisor.
    
    Returns:
        int: The largest number that divides n evenly, smaller than n.
    
    Raises:
        ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(30))  # Output: 15
```

In this script, we iterate from `n - 1` down to 1, and the first number `i` for which `n % i == 0` is the largest divisor of `n`. The `largest_divisor` function also includes input validation to ensure that `n` is a positive integer, and raises a `ValueError` otherwise.