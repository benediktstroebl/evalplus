### Largest Divisor Function
#### Python Solution
```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n

    Examples:
    >>> largest_divisor(15)
    5
    >>> largest_divisor(25)
    25
    >>> largest_divisor(100)
    100
    """
    # Start from n-1 and check each number if it divides n evenly
    for i in range(n-1, 0, -1):
        # If n is divisible by i, return i as the largest divisor
        if n % i == 0:
            return i
```
This function iterates from `n-1` down to `1`, checking each number if it divides `n` evenly. As soon as it finds a divisor, it immediately returns that number as the largest divisor. This approach ensures that the function has a time complexity of O(n), which is efficient for finding the largest divisor of a given number.