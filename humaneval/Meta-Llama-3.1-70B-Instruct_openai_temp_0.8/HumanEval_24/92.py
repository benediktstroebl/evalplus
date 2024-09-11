```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The input number
    
    Returns:
    int: The largest divisor of n, smaller than n
    """
    for i in range(n - 1, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```
This script defines the `largest_divisor` function, which iterates from `n-1` down to `2` to find the largest number that divides `n` evenly. It uses the modulo operator (`%`) to check if a number is a divisor of `n`. If a divisor is found, it is immediately returned.

Note that this function assumes that the input number `n` is at least `2`, since the largest divisor of `1` or `0` is not well-defined. If you need to handle these cases, you can add additional error checking code.