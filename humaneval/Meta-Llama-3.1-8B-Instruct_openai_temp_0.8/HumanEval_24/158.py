### Largest Divisor
#### Problem Statement
For a given number n, find the largest number that divides n evenly, smaller than n.

#### Solution
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
    n (int): The number for which to find the largest divisor.

    Returns:
    int: The largest number that divides n evenly, smaller than n.

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
```

#### Explanation
This function works by iterating from `n - 1` down to `1`, checking each number to see if it divides `n` evenly. The first number that does is the largest divisor, so the function returns it as soon as it finds one. If `n` is a prime number, the function will return `1`, which is technically correct but not necessarily the typical answer people would expect. If you want to handle prime numbers differently, you can add a special case at the beginning of the function to return `n` if it is prime.