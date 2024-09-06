```python
def fizz_buzz(n):
    return sum(any(c==7) for c in str(n) if c.isdigit()) % 2
```