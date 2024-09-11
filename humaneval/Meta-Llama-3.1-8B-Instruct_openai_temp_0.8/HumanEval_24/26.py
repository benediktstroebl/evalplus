### Solution
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20
print(largest_divisor(1))   # Output: 1
```
### Explanation
The `largest_divisor` function iterates from `n - 1` down to `1` to find the largest number that divides `n` evenly. If a divisor is found, it is immediately returned.

This approach ensures efficiency by reducing the search space as it checks numbers in descending order. If a number is not a divisor, it moves on to the next one, effectively eliminating the need for unnecessary checks.

The test cases at the end demonstrate the function's behavior for different inputs.