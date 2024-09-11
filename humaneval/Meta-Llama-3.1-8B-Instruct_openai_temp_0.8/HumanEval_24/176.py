```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n

    Example:
    >>> largest_divisor(15)
    5
    """
    # Initialize the largest divisor as 1, which is the smallest possible divisor
    largest = 1
    
    # Iterate from the largest possible divisor (n-1) to 1
    for i in range(n-1, 0, -1):
        # Check if the current number is a divisor of n
        if n % i == 0:
            # If it is, update the largest divisor and break the loop
            largest = i
            break
    
    return largest

# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(24))  # Should print 12
```

In this script, the function `largest_divisor(n)` takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It iterates from `n-1` to `1` and checks if each number is a divisor of `n`. If it finds a divisor, it updates the largest divisor and breaks the loop. Finally, it returns the largest divisor.