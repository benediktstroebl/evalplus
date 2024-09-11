```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n, smaller than n

    Example:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor to 1 (since 1 divides any number)
    largest = 1
    # Iterate from 2 to n (exclusive)
    for i in range(2, n):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, update the largest divisor
            largest = i
    return largest

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor(n)` that takes a number `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It uses a simple iteration from 2 to `n` (exclusive) to check for divisors, and updates the largest divisor whenever a larger divisor is found. The function is then tested with the example `largest_divisor(15)` to verify its correctness.