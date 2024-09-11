### Largest Divisor Function

The following Python script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`.

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): A positive integer

    Returns:
        int: The largest number that divides n evenly, smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and decrement until we find a divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(25))  # Output: 5
```

This script uses a simple loop to check all numbers smaller than `n` to see if they are divisors of `n`. It returns the first divisor it finds, which is guaranteed to be the largest divisor smaller than `n`.