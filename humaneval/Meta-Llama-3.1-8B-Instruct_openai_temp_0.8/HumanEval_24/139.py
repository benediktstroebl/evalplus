```markdown
### Largest Divisor Function

This Python function calculates the largest number that can divide a given number `n` evenly, smaller than `n`.

#### Code
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Example:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
```

#### Explanation

This function works by iterating over all numbers from `n-1` down to 1 and checking if `n` is divisible by each number. The moment it finds a number that divides `n` evenly, it returns that number as the largest divisor.

#### Example Usage

```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
print(largest_divisor(37))  # Output: 1
```
```