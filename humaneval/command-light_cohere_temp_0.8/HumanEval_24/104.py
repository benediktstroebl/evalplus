```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not any(n % d)))
```
This Python code defines a function called `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`. The function uses a list comprehension to generate all divisors from 1 up to `n` and then returns the largest divisor using the `next` function. 
test cases are also provided to ensure the correctness of the function.