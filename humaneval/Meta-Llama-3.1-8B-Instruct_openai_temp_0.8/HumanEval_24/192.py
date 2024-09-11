```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The number to find the largest divisor for.

    Returns:
        int: The largest number that divides n evenly, smaller than n.

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i


# Example usage:
print(largest_divisor(15))  # Output: 5
```

In this script, we define a function `largest_divisor(n)` that takes an integer `n` as an argument and returns the largest number that divides `n` evenly, smaller than `n`. We use a for loop to iterate from `n-1` downwards to `1`, checking if each number `i` is a divisor of `n`. As soon as we find a divisor, we return it.