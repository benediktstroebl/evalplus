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
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None  # Return None if no divisor is found
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest divisor of `n` that is smaller than `n`. The function iterates from `n-1` down to `1` and checks for divisibility using the modulo operator (`n % i == 0`). As soon as it finds a divisor, it returns that value. If no divisor is found, it returns `None`.

You can test this function with the example you provided:
```python
print(largest_divisor(15))  # Output: 5
```

Note that this function assumes that the input `n` is a positive integer. If you need to handle negative integers or non-integer inputs, you may need to modify the function accordingly.