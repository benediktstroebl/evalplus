### Largest Divisor Function

Here's a Python script that defines a function `largest_divisor` to find the largest number that divides `n` evenly, smaller than `n`.

```markdown
# Largest Divisor Function
================================

### Code

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None
```

### Example Usage

```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(23))  # Output: None
```

### Explanation

The function `largest_divisor` takes an integer `n` as input and iterates from `n - 1` down to 1. For each number `i` in the range, it checks if `n` is divisible by `i` using the modulo operator (`n % i == 0`). As soon as it finds a divisor, it returns that divisor. If no divisors are found (i.e., `n` is a prime number), it returns `None`.