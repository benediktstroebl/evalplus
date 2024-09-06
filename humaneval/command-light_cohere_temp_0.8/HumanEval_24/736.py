```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if any(n% i == 0))
```
Do you require any further assistance with writing code or have other questions related to Python or programming?