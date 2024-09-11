```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(7))   # Output: 1
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest divisor of `n`, smaller than `n`. The function uses a simple iterative approach to find the largest divisor. It starts from `n - 1` and checks each number to see if it divides `n` evenly. As soon as it finds such a number, it returns it. If no such number is found (i.e., `n` is a prime number), the function returns 1.