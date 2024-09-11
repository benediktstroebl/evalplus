```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(24))  # Output: 12
print(largest_divisor(7))   # Output: 1
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly. It uses a for loop to iterate from `n-1` down to `1` and checks each number to see if it divides `n` evenly. The first number that divides `n` evenly is the largest divisor, so it returns this number. If no divisor is found (i.e., the input is a prime number), the function returns 1, since 1 is a divisor of every number.