```python
def fizz_buzz(n):
    return sum(n < c for c in range(10) if any(i % 11 == 0 or i % 13 == 0 for i in range(10, n)))
```