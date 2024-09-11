```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n smaller than n
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

This script defines a function `largest_divisor(n)` that iterates from `n-1` down to `1`, checking each number to see if it divides `n` evenly (i.e., `n % i == 0`). As soon as it finds a divisor, it returns that number. If no divisors are found (i.e., `n` is prime), it returns `1`.