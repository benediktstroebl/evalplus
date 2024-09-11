### Largest Divisor Function
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from the largest possible divisor, which is n // 2
    for i in range(n // 2, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i
    # If no divisors are found, return 1 (1 is a divisor of every number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(16))  # Output: 8
print(largest_divisor(17))  # Output: 1
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n // 2` down to 1, checking each number to see if it is a divisor of `n`. If it finds a divisor, it returns that number as the largest divisor. If no divisors are found, it returns 1.