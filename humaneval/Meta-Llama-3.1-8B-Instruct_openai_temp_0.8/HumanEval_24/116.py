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
    # Initialize divisor as 1 (since 1 divides all numbers)
    divisor = 1
    
    # Iterate from 2 to n (exclusive) to find the largest divisor
    for i in range(2, n):
        # Check if i is a divisor of n
        if n % i == 0:
            # Update the largest divisor if i is larger
            divisor = i
    
    return divisor
```

This script uses a simple iterative approach to find the largest divisor of a given number `n`. It starts from 2 and checks each number up to `n` (exclusive) to see if it divides `n` evenly. If it does, it updates the largest divisor. Finally, it returns the largest divisor found.