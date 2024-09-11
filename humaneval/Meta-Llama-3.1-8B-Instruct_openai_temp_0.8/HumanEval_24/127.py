### Largest Divisor
#### A Python Function to Find the Largest Divisor of a Number

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Example:
        >>> largest_divisor(15)
        5
    """
    # Start checking from the largest possible divisor (n-1)
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i
    # If no divisors are found, return 1 (n is its own divisor)
    return 1

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(12))  # Output: 6
```

This function uses a loop to check all numbers smaller than `n` to find the largest one that divides `n` evenly. It starts from `n-1` (the largest possible divisor) and decrements the value until it finds a divisor. If no divisors are found, it returns 1 (since `n` is its own divisor).