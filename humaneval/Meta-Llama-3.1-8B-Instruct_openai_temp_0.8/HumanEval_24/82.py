```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    # Start checking from n-1 downwards, because we're looking for the largest divisor
    for i in range(n - 1, 0, -1):
        # Use the modulo operator (%) to check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
print(largest_divisor(25))  # Output: 25
```

This script uses a simple loop to check each number below `n` to see if it's a divisor. If it is, it returns that number. The loop starts from `n-1` and goes down to 1, checking each number to see if it's a divisor. The modulo operator (`%`) is used to check if `n` is evenly divisible by `i`. If `n` divided by `i` leaves a remainder of 0, then `i` is a divisor and the function returns it.