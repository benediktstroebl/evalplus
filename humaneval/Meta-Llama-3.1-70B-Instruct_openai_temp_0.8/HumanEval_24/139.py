```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The number to find the largest divisor for.
    
    Returns:
    int: The largest number that divides n evenly, smaller than n.
    """
    # Start from n-1 and iterate downwards to find the largest divisor
    for i in range(n-1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If it does, return i as the largest divisor
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It uses a simple iterative approach, starting from `n-1` and checking each number to see if it divides `n` evenly. The first such number it finds is the largest divisor, which it then returns.