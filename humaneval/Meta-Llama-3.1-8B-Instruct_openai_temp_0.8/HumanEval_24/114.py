### Largest Divisor Script
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

# Test the function
print(largest_divisor(15))  # Output: 5
```
This script defines a function `largest_divisor` that takes an integer `n` as input. It iterates from `n - 1` down to 1, checking if each number is a divisor of `n` by using the modulo operator (`n % i == 0`). The first number that meets this condition is returned as the largest divisor.

Note that this solution has a time complexity of O(n), which may not be efficient for large inputs. A more efficient approach would be to use the floor of the square root of `n` as the upper bound for the loop, as any factor larger than that would have a corresponding factor smaller than the square root. However, this simple solution is sufficient for smaller inputs.