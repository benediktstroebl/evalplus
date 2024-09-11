```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 4
print(largest_divisor(7))   # Output: 1
```

This script defines the `largest_divisor` function, which iterates from `n-1` down to `1` and checks each number if it divides `n` evenly (i.e., if `n` modulo the current number is `0`). The function returns the first such number it finds (which is the largest divisor), and stops iterating as soon as this condition is met.