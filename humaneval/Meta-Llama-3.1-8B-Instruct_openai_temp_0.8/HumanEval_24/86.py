```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n.
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and check if it's a divisor of n
    for i in range(n-1, 0, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes a number `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by starting from `n-1` and checking if each number is a divisor of `n`. If a number is a divisor, it is immediately returned. The function is then tested with the example `largest_divisor(15)`.