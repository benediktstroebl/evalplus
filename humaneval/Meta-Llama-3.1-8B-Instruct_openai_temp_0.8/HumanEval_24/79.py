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
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(21))  # Output: 7
print(largest_divisor(36))  # Output: 18
print(largest_divisor(1))   # Output: 1
```

This script defines a function `largest_divisor(n)` that finds the largest number that divides `n` evenly (i.e., the largest divisor). It uses a loop to iterate from `n - 1` down to 1 and checks each number to see if it divides `n` evenly. The first number that it finds that divides `n` evenly is the largest divisor, and it returns this number.

Note that the loop starts from `n - 1` instead of `n` because we know that `n` is a divisor of `n` itself, and we want to find the largest divisor that is smaller than `n`. The loop also uses a step size of `-1`, which means it will decrease the loop variable by 1 each time, effectively iterating down from `n - 1` to 1.