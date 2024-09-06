```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not operator.is_divisible(n, d)) or n)

def is_divisible(n: int, d: int) -> bool:
    return n % d == 0
```
This Python script defines a function `largest_divisor(n)` that finds the largest divisor of the given number `n`. The `is_divisible(n, d)` function checks whether `d` is a divisor of `n`. This function uses the `next` function with a generator expression to iterate through potential divisors of the number until finding the largest one.  This's purpose is to solve the problem of finding the largest divisor of a given number.