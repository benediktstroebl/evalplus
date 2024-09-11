```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The number to find the largest divisor for.
    
    Returns:
    int: The largest number that divides n evenly, smaller than n.
    
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest one
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(16))  # Output: 8
print(largest_divisor(17))  # Output: 1
```

This script defines a function `largest_divisor` that finds the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n - 1` down to `1`, checking each number to see if it's a divisor of `n`. The first divisor it finds is the largest one, which it then returns.

When you run this script, it prints the largest divisor for each of the numbers `15`, `16`, and `17`, demonstrating the function's correctness.