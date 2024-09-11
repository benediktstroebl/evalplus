### Solution

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest number that divides n evenly.
    """
    # Start from n-1, as n itself cannot be the divisor we're looking for
    for i in range(n-1, 0, -1):
        # Check if i divides n evenly
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
```

### Explanation

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly. The function iterates from `n-1` down to 1, and for each number `i`, it checks if `n` is divisible by `i` by verifying if the remainder of `n` divided by `i` is 0. If `n` is divisible by `i`, the function immediately returns `i` as the result. The test case `largest_divisor(15)` confirms that the function works as expected, returning 5 as the largest divisor of 15.