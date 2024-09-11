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
    # We start checking from n-1 downwards, because the problem guarantees a divisor smaller than n exists
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, then i is a divisor of n
        if n % i == 0:
            # As we're checking in descending order, the first divisor we find is the largest
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
```
This script defines the `largest_divisor` function, which finds the largest divisor of a given number `n`. The function iterates from `n-1` downwards to find the first number that divides `n` evenly, and returns that number as the largest divisor. The example usage is also included in the code block.