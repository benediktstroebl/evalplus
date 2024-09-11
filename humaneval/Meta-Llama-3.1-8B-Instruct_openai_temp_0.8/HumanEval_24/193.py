```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): A positive integer

    Returns:
        int: The largest divisor of n

    Example:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and find the first number that divides n evenly
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

# Test the function
if __name__ == "__main__":
    print(largest_divisor(15))  # Output: 5
```

This script uses a simple loop to iterate from `n-1` down to 1, checking if each number is a divisor of `n`. The first number it finds that is a divisor is the largest one, which is returned.