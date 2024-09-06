Here is a self-contained Python script that defines a function to find the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), n)
```
The function uses the `next()` function with a generator expression `(d for d in range(1, n+1) if not n % d)` to generate the largest divisor of `n` that doesn't divide `n` by the remainder. The `return` statement returns the result of the first matching number, which is also `n` if no larger number exists.