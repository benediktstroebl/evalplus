```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
print(largest_divisor(13))  # Output: 1
```

In this script, the `largest_divisor` function iterates over all numbers smaller than `n` in reverse order. As soon as it finds a number that divides `n` evenly (i.e., the remainder `n % i` is 0), it returns that number. If no such number is found, it returns 1, since 1 divides any number.

However, this solution is not very efficient because it checks all numbers smaller than `n`. A more efficient approach is to start from `n // 2` (integer division by 2), since any divisor larger than that would have a corresponding divisor smaller than `n // 2`.

Here's an improved version of the function:

```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i
    return 1

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 6
print(largest_divisor(13))  # Output: 1
```

This version of the function is more efficient because it only checks numbers up to `n // 2`, which reduces the number of iterations significantly.