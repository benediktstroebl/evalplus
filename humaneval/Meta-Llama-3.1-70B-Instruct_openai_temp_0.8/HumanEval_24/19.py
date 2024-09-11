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
    # Start from the largest possible divisor
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return i as the largest divisor
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

This script defines the `largest_divisor` function, which iterates over numbers smaller than `n` in descending order and checks if they are divisors of `n` by using the modulo operator (`n % i == 0`). The first divisor it finds is the largest one, so it immediately returns that value.

Note: This function has a time complexity of O(n), which may not be efficient for large inputs. A more efficient solution would be to only check up to the square root of `n`, as any factor larger than that would have a corresponding factor smaller than the square root.