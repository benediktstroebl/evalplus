```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    >>> largest_divisor(15)
    5
    """
    # Start from n-1, as the problem states we need a divisor smaller than n
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as it's the largest one
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines the `largest_divisor` function, which iterates from `n-1` down to 1 to find the largest number that divides `n` evenly. The function uses the modulo operator (`%`) to check if a number `i` is a divisor of `n`. As soon as it finds a divisor, it returns that number. The script also includes a test case to verify the function's correctness.