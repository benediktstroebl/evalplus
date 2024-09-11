### Largest Divisor Function
#### Description
This script defines a function `largest_divisor` that finds the largest number that divides a given number `n` evenly, smaller than `n`.

#### Code

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
```

#### Explanation
This function works by iterating from `n-1` down to `1` and checking if each number is a divisor of `n`. The first such number found is the largest divisor smaller than `n`, so it is immediately returned.