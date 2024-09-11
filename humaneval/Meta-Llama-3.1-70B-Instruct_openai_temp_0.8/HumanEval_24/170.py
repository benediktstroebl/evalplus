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
    return 1  # Return 1 if no other divisors are found

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(7))   # Output: 1
```

This script defines the `largest_divisor` function, which takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a simple loop to iterate from `n-1` down to 1, checking each number to see if it divides `n` evenly (i.e., if the remainder is 0). If it finds a divisor, it returns that number immediately. If it doesn't find any divisors (which would only happen for the number 1), it returns 1.