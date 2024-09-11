```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
print(largest_divisor(16))  # Output: 8
print(largest_divisor(17))  # Output: 1 (since 17 is a prime number)
```

This script defines a function `largest_divisor` that takes a number `n` as input and returns the largest divisor of `n` that is smaller than `n`. It does this by iterating through numbers from `n - 1` down to 1 and checking if each number is a divisor of `n` using the modulo operator (`n % i == 0`). The first divisor found is returned. 

Note that this function assumes that `n` is a non-negative integer. If `n` can be negative or a non-integer, you may need to modify the function accordingly.