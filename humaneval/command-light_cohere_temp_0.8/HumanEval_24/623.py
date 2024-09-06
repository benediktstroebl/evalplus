```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if all(n% d == 0)))
```
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest integer which divides the given number evenly (i. The code uses the `next()` to generate the list of divisors and check if all elements in the list divide the given number evenly. 

Additionally, it uses the `all` function to check if the condition is satisfied for any element in the list.