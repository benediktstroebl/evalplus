```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Start checking from n-1
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(24))  # Expected output: 12
```

This Python script defines the function `largest_divisor(n)` which returns the largest number that divides `n` evenly and is smaller than `n`. The function starts checking from `n-1` down to `1`, returning the first number that divides `n` evenly. The test cases are provided at the end of the script.