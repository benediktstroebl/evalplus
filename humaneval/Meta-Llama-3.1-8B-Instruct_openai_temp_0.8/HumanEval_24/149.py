```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    Parameters:
    n (int): The number to find the largest divisor for
    Returns:
    int: The largest divisor of n
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly. It iterates from `n - 1` down to `1` and checks if each number is a divisor of `n` by using the modulo operator (`%`). If a divisor is found, it is immediately returned. If no divisors are found (which should only happen for 1, as 1 divides all numbers), it returns `1`.