Here is a self-contained Python script with a function that solves the problem of finding the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    return next((i for i in range(1, n + 1) if not n % i), 1)
```

This function uses the built-in `next()` function and a generator expression to iterate through numbers from 1 up until the input number is reached. The function returns the value of the largest divisor found.