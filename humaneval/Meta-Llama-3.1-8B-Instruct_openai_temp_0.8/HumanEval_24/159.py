```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number
    
    Returns:
        int: The largest divisor of n smaller than n
    
    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(16))  # Output: 8
print(largest_divisor(17))  # Output: 1
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, which is smaller than `n`. The function iterates from `n-1` down to 1, checks if each number is a divisor of `n` by using the modulo operator (`%`), and returns the first number that is a divisor.