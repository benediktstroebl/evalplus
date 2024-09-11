### Largest Divisor Function
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
    # Start from n - 1 and check if each number is a divisor
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```
This script defines a function `largest_divisor` that finds the largest divisor of a given number `n`. It iterates from `n - 1` down to 1, checking if each number is a divisor of `n` using the modulo operator `%`. If a number is found to be a divisor, it is immediately returned.