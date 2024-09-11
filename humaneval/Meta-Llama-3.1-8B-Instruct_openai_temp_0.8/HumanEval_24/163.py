```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest number that divides n evenly, smaller than n.
    
    Example:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

In this script, the function `largest_divisor` iterates from `n-1` down to `1`, checking each number to see if it divides `n` evenly by using the modulus operator (`%`). The first number it finds that divides `n` evenly is the largest divisor of `n` smaller than `n`, and it returns this number.