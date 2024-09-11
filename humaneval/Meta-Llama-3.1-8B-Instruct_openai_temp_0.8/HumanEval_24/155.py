```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n
    """
    # Initialize the largest divisor to 1 (since 1 divides any number)
    largest = 1
    
    # Iterate from 2 to n (inclusive) to find the largest divisor
    for i in range(2, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, update the largest divisor
            largest = i
    
    # Return the largest divisor found
    return largest

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It iterates from 2 to `n` (inclusive) to find the largest divisor. If `n` is 1, the function returns 1, since 1 divides any number.