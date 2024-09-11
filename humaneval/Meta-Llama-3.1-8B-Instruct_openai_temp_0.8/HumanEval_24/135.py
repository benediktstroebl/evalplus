```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for

    Returns:
        int: The largest divisor of n

    >>> largest_divisor(15)
    5
    """
    # Initialize the largest divisor as 1 (since 1 divides every number)
    largest = 1
    
    # Iterate from 2 to n (inclusive)
    for i in range(2, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, update the largest divisor
            largest = i
    
    return largest

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(10))  # Expected output: 5
print(largest_divisor(7))   # Expected output: 1
```

This script defines a function `largest_divisor` that takes a number `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It iterates from 2 to `n` and checks each number to see if it is a divisor of `n`. If it is, it updates the largest divisor. The function returns the largest divisor found.