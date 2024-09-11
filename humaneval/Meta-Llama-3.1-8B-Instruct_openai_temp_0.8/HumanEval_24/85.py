```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start checking from the largest possible divisor (n // 2)
    # We only need to check up to n // 2 because a larger factor of n must be a multiple of smaller factor that has already been checked
    for i in range(n // 2, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, it's the largest one, so return it
            return i
    # If no divisors are found, return 1 (1 is a divisor of every number)
    return 1


# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```

This script defines a function `largest_divisor(n)` that finds the largest number that divides `n` evenly, smaller than `n`. It does this by iterating from the largest possible divisor (`n // 2`) down to 1, checking each number to see if it's a divisor of `n`. If it is, it's the largest one, so it's returned. If no divisors are found, the function returns 1 (which is a divisor of every number). The example usage at the end shows how to use this function.