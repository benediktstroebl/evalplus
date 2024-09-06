```python
def largest_divisor(n):
    """ Returns the largest divisor of n <= n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through factors of `n` in the range of `1` to `n` and returns the largest factor that yields a remainder of zero when divided by `n`. This is the largest divisor that is less than or equal to `n`.