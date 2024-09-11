### Find the Largest Divisor of a Number

The following Python function finds the largest number that evenly divides a given number `n`, where the divisor is smaller than `n`.

```markdown
### Code

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor for.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
```

### Explanation

This function works by iterating from `n-1` down to `1` (excluding `n` itself). For each number `i` in this range, it checks if `n` is divisible by `i` by using the modulus operator (`%`). If `n` is divisible by `i`, then `i` is the largest number that divides `n` evenly and smaller than `n`, so the function returns `i`.

### Example Usage

```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
print(largest_divisor(7))   # Output: 1
```

### Optimization

Note that this function has a time complexity of O(n), where n is the given number. This is because in the worst case, the function needs to iterate from `n-1` down to `1`. However, this is still efficient for most practical purposes. If you need to find the largest divisor for very large numbers, you may want to consider using a more efficient algorithm, such as the one based on prime factorization or the one based on the Pollard's rho algorithm.