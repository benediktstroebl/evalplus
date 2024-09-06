```python
def fizz_buzz(n: int) -> int:
    return sum([7] * x for x in range(2, n + 1) if x % 11 or 13 == 0)
```