```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
    n (int): The number to find the largest divisor for.
    
    Returns:
    int: The largest number that divides n evenly, smaller than n.
    """
    # Start from n-1 and work our way down to 1
    for i in range(n-1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            # If it does, return i as the largest divisor
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(30))  # Output: 15
print(largest_divisor(7))   # Output: 1
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a simple iterative approach, starting from `n-1` and working its way down to `1`, checking each number to see if it divides `n` evenly. The first number that does is returned as the largest divisor.