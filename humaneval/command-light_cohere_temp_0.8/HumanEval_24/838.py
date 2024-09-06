Here's the self-contained Python script with a function that finds the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number which divides the given number evenly, smaller than n."""
    while n % 2 == 0:
        n /= 2
    return n
```

This function uses a while loop to repeatedly divide by 2 until the remainder becomes non-zero, then returns the current value of n as the largest divisor.