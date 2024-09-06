```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and d != 1), n)
```
Do you need assistance with anything else related to code?