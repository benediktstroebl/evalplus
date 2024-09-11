### Largest Divisor Function in Python
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    if n == 1:
        # 1 is a divisor of every number, but it's not considered a "largest" divisor in this context.
        # So, we return n instead.
        return n
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


# Test the function
print(largest_divisor(15))  # Output: 5
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly and is smaller than `n`. It uses a for loop to iterate from `n-1` down to `1` and checks if each number is a divisor of `n` using the modulo operator (`%`). As soon as it finds a divisor, it returns the divisor. If `n` is 1, it returns `n` (but this is technically a special case, since 1 is a divisor of every number, but it's not considered a "largest" divisor in this context).