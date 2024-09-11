```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n, smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    # Start checking from n-1, because n itself cannot be the largest divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Return the first divisor found, which will be the largest
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input, and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a loop to check all numbers from `n-1` down to 1, and returns the first number that is a divisor of `n`. The test case at the end of the script demonstrates the function's behavior with the input `15`, which should output `5`.