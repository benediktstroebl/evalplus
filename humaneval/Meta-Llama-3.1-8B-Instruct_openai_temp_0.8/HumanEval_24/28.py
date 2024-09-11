### Largest Divisor
#### A Python Function to Find the Largest Divisor of a Number

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Example:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor to 1
    largest = 1
    
    # Iterate over all numbers from 2 to n (inclusive)
    for i in range(2, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, update the largest divisor
            largest = i
    
    # Return the largest divisor
    return largest

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides `n` evenly, smaller than `n`. It uses a simple iteration to find the largest divisor by checking if each number from 2 to `n` is a divisor of `n`. The function is then tested with the example input `15`.