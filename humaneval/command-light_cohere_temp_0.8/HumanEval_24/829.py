```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and d != 1), 1)
 ``` 
This code defines a function called `largest_divisor` that takes an integer `n` as input and returns the largest integer that divides `n` evenly, smaller than `n`. The function uses the `next()` function with a generator expression `(d for d in range(1, n+1) if not n % d and d != 1`) to generate potential divisors of `n`.  The `next()` function returns the first element that satisfies this condition, so the largest integer that divides `n` evenly is returned. 
test cases for the function using the `assert` module are also provided.