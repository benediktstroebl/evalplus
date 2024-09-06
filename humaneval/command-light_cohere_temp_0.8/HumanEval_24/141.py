Here is a Python script with a self-contained function that solves the problem of finding the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not n % d), n)
```

This function efficiently finds the largest divisor of the number n by using a generator expression and the next() function. It starts from the Either smallest divisor and continues up to the number n, ensuring that the divisor is less than n.