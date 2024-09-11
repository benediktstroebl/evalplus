```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n - 1` down to `1` and checks if `i` is a divisor of `n` by using the modulo operator (`%`). If `n % i == 0`, then `i` is a divisor of `n`, and the function returns `i`.

You can save this script to a file, for example, `largest_divisor.py`, and run it using Python, for example, `python largest_divisor.py`. The script will print the largest divisor of `15`, which is `5`.