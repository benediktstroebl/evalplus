Here is a Python script that contains a self-contained function that finds the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    return next((d for d in xrange(n+1) if not operator.isinstance(d, n % d == 0)) or n
```

This function uses the Python next() generator to iterate through the numbers from 1 to n, and checks if each number is a divisor of n. The function returns the simple cases: either the number is a divisor or it is equal to n.