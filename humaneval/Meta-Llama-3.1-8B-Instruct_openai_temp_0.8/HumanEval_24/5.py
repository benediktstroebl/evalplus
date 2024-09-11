### Largest Divisor Finder
#### Problem Statement
For a given number n, find the largest number that divides n evenly, smaller than n.

#### Solution

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor of.

    Returns:
    int: The largest number that divides n evenly, smaller than n.
    """
    # Starting from n-1, find the first number that divides n evenly
    for i in range(n-1, 0, -1):
        if n % i == 0:
            # If a number is found, return it as the largest divisor
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n-1` down to 1 and checks each number to see if it divides `n` evenly. As soon as it finds a number that does, it returns that number as the largest divisor.