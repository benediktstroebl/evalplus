```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The number for which to find the largest divisor.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

print(largest_divisor(15))  # Output: 5
```

In this code:

- We start from `n - 1` and iterate downwards to `1`.
- For each number `i` in this range, we check if `n` is divisible by `i` by using the modulus operator (`%`).
- The first `i` for which `n % i == 0` is the largest number that divides `n` evenly, smaller than `n`.
- We immediately return this `i` as the result.

This solution has a time complexity of O(n) because in the worst-case scenario (when `n` is a prime number), we have to iterate from `n - 1` down to `1`. For larger numbers, a more efficient solution could be implemented using a different approach, such as only iterating up to the square root of `n`.