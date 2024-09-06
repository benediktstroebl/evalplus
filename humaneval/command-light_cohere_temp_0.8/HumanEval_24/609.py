```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if all(n % d == 0)))
```
This code defines a function called `largest_divisor` that takes an integer `n` as input and returns the largest divisor of `n` (the largest number that divides evenly into `n`). The function uses a generator expression to iterate through numbers from 1 to `n` and checks if all divisions of the number are equal to 0 using the `all` function. The `next` function then returns the unique divisor, which is the largest number.