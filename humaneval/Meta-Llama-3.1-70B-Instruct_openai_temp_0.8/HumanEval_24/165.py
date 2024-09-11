```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    >>> largest_divisor(17)
    1
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
```
In this script, the function `largest_divisor` takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating over all numbers from `n - 1` down to `1` and checking if `n` is divisible by each number. The first number that divides `n` evenly is the largest divisor, so the function returns it as soon as it finds one.

Note: The function assumes that the input is a positive integer. If the input can be zero or negative, or if it can be a non-integer, you should add error checking code to handle these cases.