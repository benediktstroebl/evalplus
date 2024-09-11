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
    # Start checking from n-1, because the divisor cannot be n itself
    for i in range(n-1, 0, -1):
        # If n is divisible by i, then i is the largest divisor
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```
This script defines the `largest_divisor` function, which takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates over numbers from `n-1` down to 1, checking if each number divides `n` evenly. If it finds a divisor, it immediately returns that divisor. The script also includes some test cases at the end to demonstrate its usage.