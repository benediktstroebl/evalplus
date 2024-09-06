Here is a Python script with a self-contained function that finds the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if n % i == 0)
```

This function uses the Python next() function with a generator expression in order to find the largest divisor of a given number 'n'. It starts from 1 and loops until reaching a number that divides the number 'n' evenly.  The the highest divisor found will be returned as the output of the function.