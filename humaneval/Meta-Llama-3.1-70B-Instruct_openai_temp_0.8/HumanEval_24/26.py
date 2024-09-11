```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n that is smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(25))  # Output: 5
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest divisor of `n` that is smaller than `n`. It iterates from `n - 1` down to `1` and checks if `n` is divisible by the current number `i`. As soon as it finds a divisor, it returns that number. The function includes a docstring with a description, argument and return information, and examples of usage.