### Largest Divisor Function
#### Python Implementation
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n.

    Example:
    >>> largest_divisor(15)
    5
    """
    # Iterate from n-1 to 1 in reverse order to find the largest divisor
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i
    # If no divisors are found, return 1 (since 1 is a divisor of every number)
    return 1
```

### Example Usage
```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
print(largest_divisor(12))  # Output: 6
```