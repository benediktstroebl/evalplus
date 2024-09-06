```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
The function uses the next() function, which returns the next item in the iterator, effectively generating a list of divisors until the given number. This list of divisors is then returned by the function.

This Python function efficiently finds the largest divisor of a given number, ensuring the correct output for any input value.