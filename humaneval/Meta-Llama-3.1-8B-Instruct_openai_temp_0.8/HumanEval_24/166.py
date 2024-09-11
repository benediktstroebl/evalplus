```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n.

    >>> largest_divisor(15)
    5
    """
    # Start from the largest possible divisor, which is n // 2
    for i in range(n // 2, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i
    # If no divisor is found, return 1 (1 divides every number)
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(20))  # Output: 20
```

This script defines a function `largest_divisor(n)` that finds the largest number that divides `n` evenly, smaller than `n`. The function starts from the largest possible divisor, which is `n // 2`, and checks each number down to 1. The first number that is a divisor of `n` is returned. If no divisor is found, the function returns 1 (1 divides every number). The script also includes some test cases to demonstrate the function's usage.