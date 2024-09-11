```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The input number

    Returns:
        int: The largest number that divides n evenly, smaller than n

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(17))  # Output: 1
```

This script defines a function `largest_divisor(n)` that finds the largest number `i` less than `n` such that `n` is divisible by `i`. It uses a for loop to check all numbers from `n-1` down to 1. As soon as it finds a number `i` that divides `n` evenly (`n % i == 0`), it returns `i`.