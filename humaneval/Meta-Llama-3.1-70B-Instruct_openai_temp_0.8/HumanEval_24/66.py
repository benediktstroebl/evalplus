```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(21))  # Output: 7
print(largest_divisor(30))  # Output: 15
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, which is smaller than `n`. The function works by iterating over the numbers from `n-1` to `1` in reverse order and checking if `n` is divisible by each number. As soon as it finds a number that divides `n` evenly, it returns that number.

The script also includes some test cases to demonstrate the function's usage.