```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None

# Example usage:
print(largest_divisor(15))  # Outputs: 5
```

This script works by looping over all numbers from n-1 down to 1, checking if the current number is a divisor of n by using the modulus operator (`n % i == 0`). If it finds a divisor, it immediately returns it. If it doesn't find any divisors after checking all numbers, it returns None.