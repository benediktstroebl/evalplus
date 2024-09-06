```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if any(n % i == 0))
```
This function uses the built-in generator expression `range(1, n+1)` to generate all numbers from 1 to `n`, and then uses the `any()` function along with the membership test `in range(1, n+1) if divided evenly by n. The function returns the partnership with the largest divisor of n.