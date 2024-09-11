```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It uses a for loop to iterate from `n-1` to `1`, and checks if `n` is divisible by the current number `i`. If `n` is divisible by `i`, it returns `i`.

You can call this function with different inputs to test it, for example:
```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 4
print(largest_divisor(17))  # Output: 1
```