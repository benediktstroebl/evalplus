```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest divisor of n that is less than n.
    Returns -1 if no such selected
    """
    # Initialize the largest divisor candidate
    max_divisor = 1
    # Search for the largest divisor in descending order
    while n % max_divisor == 0 and max_divisor <= n:
        max_divisor += 1
    return max_divisor
```