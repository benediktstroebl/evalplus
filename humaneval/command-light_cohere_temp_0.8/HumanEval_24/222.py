```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), 0)
```
This Python function, `largest_divisor`, takes an integer `n` as input and returns the largest integer that evenly divides `n`. The function uses a generator expression to find the largest such divisor. The use of the specific testing to verify its correctness, you can add additional test cases within the `test` block.