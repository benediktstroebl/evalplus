```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), n)
```
Do you require assistance with any other programming concepts or tasks?