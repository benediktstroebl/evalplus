```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number for which to find the largest divisor.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

    Raises:
    ValueError: If n is less than 2.
    """

    if n < 2:
        raise ValueError("Input number should be greater than 1")

    # Start checking from the next smaller number
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor(n)` that finds the largest divisor of `n` smaller than `n` itself. It does this by iterating over all numbers smaller than `n` and checking if they are divisors of `n`. As soon as it finds one, it returns it, since we're starting from the largest possible divisor and moving downwards. The script also includes a check to ensure that the input number is greater than 1.