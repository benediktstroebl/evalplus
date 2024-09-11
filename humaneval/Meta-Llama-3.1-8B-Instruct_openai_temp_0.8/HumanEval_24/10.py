```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n

    >>> largest_divisor(15)
    5
    """
    # Initialize the largest divisor as 1, since 1 divides any number
    largest = 1
    
    # Iterate from 2 to n (exclusive) to check for divisors
    for i in range(2, n):
        # Check if the current number is a divisor of n
        if n % i == 0:
            # If it is, update the largest divisor
            largest = i
    
    # Return the largest divisor found
    return largest

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(32))  # Output: 16
print(largest_divisor(17))  # Output: 1
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from 2 to `n-1` and checks for each number if it is a divisor of `n`. If it finds a divisor, it updates the largest divisor. Finally, it returns the largest divisor found.