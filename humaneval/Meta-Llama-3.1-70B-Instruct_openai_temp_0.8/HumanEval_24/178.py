```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The number for which to find the largest divisor.
    
    Returns:
    int: The largest number that divides n evenly, smaller than n.
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Expected output: 5
```

This script works by iterating over all numbers smaller than `n` in descending order. As soon as it finds a number that divides `n` evenly (i.e., the remainder of `n` divided by the number is 0), it returns that number. This approach ensures that the function always returns the largest divisor smaller than `n`.