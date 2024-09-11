```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The input number.

    Returns:
    int: The largest divisor of n, smaller than n.
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(30))  # Output: 15
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating over all numbers from `n-1` down to `1`, checking if each number is a divisor of `n` (i.e., if `n` divided by the number leaves no remainder), and returning the first such divisor it finds.

The script also includes example usage of the `largest_divisor` function, demonstrating how to call it with different inputs and print the results.