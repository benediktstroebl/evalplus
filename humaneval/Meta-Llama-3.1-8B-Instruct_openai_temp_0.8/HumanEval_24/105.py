```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 4
print(largest_divisor(13))  # Output: 1
```

This script defines a function `largest_divisor` that takes an integer `n` as input. It iterates from `n-1` down to 1 and checks for each number if it is a divisor of `n`. The first such number it finds is the largest divisor of `n` smaller than `n`, which it returns. If no such number is found, it means that `n` is a prime number, in which case the function returns 1.