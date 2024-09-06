```python
def fizz_buzz(n: int) -> int:
    if n < 7: return 0
    return 2 if any(d == 7 for d in range(1, n)) else 3
```