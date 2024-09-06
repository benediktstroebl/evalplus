```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
The above code defines a Python function `largest_divisor` that takes an integer `n` as input and returns the largest divisor of the number n (i. The function uses a next() generator expression to iterate through the numbers from 1 up and checks if the given number divides the input number `n` evenly.