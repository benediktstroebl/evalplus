```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d))
```

This function, `largest_divisor`, takes an integer `n` as input and returns the largest divisor of `n`, which is the largest positive integer that does not leave a remainder when dividing `n` by it. The `next()` function with a generator expression `(d for d in range(1, n+1))` generates a list of integers from 1 to `n` (inclusive) and then returns the first element that does not leave a remainder when dividing `n` by it. 
This approach has an time complexity of O(n) and is self-contained within the Python language, meaning it does not rely on any external functions or modules.