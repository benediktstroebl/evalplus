```python
def largest_divisor(n: int) -> int:
    """ 
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number to find the largest divisor of.

    Returns:
    int: The largest divisor of n.

    Examples:
    >>> largest_divisor(15)
    5
    >>> largest_divisor(10)
    5
    >>> largest_divisor(7)
    1
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```
This script uses a loop to iterate over all numbers smaller than `n`. For each number, it checks if it is a divisor of `n` by using the modulo operator (`%`). If it is a divisor, it returns that number. This process stops as soon as it finds a divisor, because it's guaranteed that `n` will have at least one divisor (itself), and we're checking `n` itself at the end of the range.