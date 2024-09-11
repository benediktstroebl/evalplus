```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
```

You can use this function by calling it with a number, like this: `print(largest_divisor(15))` which will output `5`.

This function works by iterating over all numbers from `n-1` down to `1` and checking if `n` is divisible by the current number. As soon as it finds a number that `n` is divisible by, it returns that number. The `range(n-1, 0, -1)` function generates numbers from `n-1` down to `0`, decreasing by 1 each time, so we don't need to manually decrement the counter variable.