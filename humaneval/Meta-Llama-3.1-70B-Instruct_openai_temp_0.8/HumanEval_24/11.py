```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The number to find the largest divisor for.
    
    Returns:
    int: The largest number that divides n evenly, smaller than n.
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(20))  # Expected output: 10
print(largest_divisor(31))  # Expected output: 1
```

This script defines the `largest_divisor` function, which iterates from `n-1` down to `1` to find the largest number that divides `n` evenly (i.e., with a remainder of 0). The function returns the first (and hence largest) divisor it finds.

The script also includes some test cases to demonstrate the function's behavior.