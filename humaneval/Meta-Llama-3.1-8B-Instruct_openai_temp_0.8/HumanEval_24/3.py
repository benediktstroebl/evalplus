## Largest Divisor Function
The following Python script defines a function `largest_divisor` that finds the largest number that divides a given number `n` evenly, smaller than `n`.

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and go down to 1
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i
    # If no divisors are found, return 1 (by default)
    return 1

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(10))  # Expected output: 5
print(largest_divisor(7))   # Expected output: 1
```

This script uses a simple loop to iterate from `n-1` down to 1, checking each number to see if it's a divisor of `n`. If it finds a divisor, it returns that number as the largest divisor. If it doesn't find any divisors, it returns 1 by default.