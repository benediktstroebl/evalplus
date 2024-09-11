```python
def largest_divisor(n: int) -> int:
    """ 
    For a given number n, finds the largest number that divides n evenly, smaller than n.

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
    return None

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(20))  # Expected output: 10
```

This script defines a function `largest_divisor` that takes an integer `n` as input. It iterates over the numbers from `n-1` down to 1 and checks if each number is a divisor of `n` by using the modulus operator `%`. The first number it finds that is a divisor of `n` is the largest divisor smaller than `n`, which it returns. If `n` is a prime number, the function will return `None` because there is no divisor smaller than `n` itself.