```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(30))  # Output: 15
```

This script uses a simple iterative approach to find the largest divisor of a given number `n`. It starts from `n - 1` and goes down to 1, checking each number to see if it divides `n` evenly. As soon as it finds a number that does, it returns that number. This is done in a single pass through the possible numbers, making it efficient for large inputs.