```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The input number
    
    Returns:
    int: The largest divisor of n smaller than n
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None
```

This script defines a function `largest_divisor(n)` that iterates over all numbers from `n-1` down to 1 and checks if each number is a divisor of `n`. The first divisor it finds is the largest one, and it returns that number. If `n` itself is a prime number (i.e., its only divisors are 1 and itself), it will return `None`.