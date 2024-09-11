```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(100))  # Output: 50
```

In this script, we define a function `largest_divisor(n)` that takes an integer `n` as input. The function iterates through numbers from `n-1` down to 1, checking each number to see if it is a divisor of `n` by using the modulo operator (`%`). When it finds a divisor, it immediately returns that divisor. If it reaches 1 without finding a divisor (which would be the case for a prime number), it returns 1.