### Largest Divisor Function

The following Python script defines a function `largest_divisor` that finds the largest number that divides a given number `n` evenly, smaller than `n`.

```markdown
### Code

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
    # Find the largest number that divides n evenly, smaller than n
    # We can use a loop to check all numbers smaller than n in reverse order
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i
    
    # If no divisors are found, return 1 (1 is a divisor of all numbers)
    return 1
```

### Example Usage

```python
# Test the function with examples
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
print(largest_divisor(16))  # Output: 8
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a loop to check all numbers smaller than `n` in reverse order and returns the first number that is a divisor of `n`. If no divisors are found, the function returns 1, as 1 is a divisor of all numbers. The script also includes example usage of the function with different inputs.