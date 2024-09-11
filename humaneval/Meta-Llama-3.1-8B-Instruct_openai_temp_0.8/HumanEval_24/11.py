### Largest Divisor of a Number
#### Problem Description
Find the largest number that divides a given number `n` evenly, smaller than `n`.

#### Solution
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
    n (int): The input number

    Returns:
    int: The largest divisor of n, smaller than n

    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(7))   # Output: 1
```

This script uses a for loop to iterate from `n-1` down to 1, checking each number if it is a divisor of `n`. The first number that satisfies this condition is returned as the largest divisor. If no divisors are found (i.e., `n` is a prime number), the function returns 1.