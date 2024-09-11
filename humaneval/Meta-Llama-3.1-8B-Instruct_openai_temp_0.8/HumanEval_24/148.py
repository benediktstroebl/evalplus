### Solution
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
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i
    return None
```

### Explanation

This function works by iterating over all numbers from `n-1` down to `1`. For each number `i`, it checks if `i` is a divisor of `n` by using the modulo operator (`n % i == 0`). If `i` is a divisor, the function immediately returns `i` as the largest divisor. If no divisors are found, the function returns `None`.

### Example Usage
```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20 (since 20 is the largest divisor of itself)
```