```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.
    """
    # Start from n-1 and decrement by 1 until we find a divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i
            return i

# Test the function
print(largest_divisor(15))  # Should print 5
print(largest_divisor(17))  # Should print 1
print(largest_divisor(24))  # Should print 12
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function works by starting from `n-1` and decrementing by 1 until it finds a divisor of `n`. The script also includes some test cases to demonstrate the function's correctness.