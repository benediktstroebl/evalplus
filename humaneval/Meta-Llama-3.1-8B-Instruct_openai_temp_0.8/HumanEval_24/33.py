### Largest Divisor Python Script
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
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i


if __name__ == "__main__":
    # Test the function
    print(largest_divisor(15))  # Output: 5
    print(largest_divisor(10))  # Output: 5
    print(largest_divisor(17))  # Output: 1
```
This script defines a function `largest_divisor(n)` that finds the largest number that divides `n` evenly, smaller than `n`. It does this by iterating from `n-1` down to `1` and checking if each number is a divisor of `n`. The first number it finds that is a divisor is the largest divisor of `n`.