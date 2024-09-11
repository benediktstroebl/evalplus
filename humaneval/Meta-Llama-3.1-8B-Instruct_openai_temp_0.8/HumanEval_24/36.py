```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number
    
    Returns:
        int: The largest divisor of n smaller than n
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(20))  # Output: 20
```

This script uses a simple iterative approach to find the largest divisor of `n`. It starts from `n-1` and checks each number to see if it divides `n` evenly. As soon as it finds a number that does, it returns that number. If it doesn't find any divisors smaller than `n`, it returns 1 (which is a divisor of every number).