```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if all(n % d == 0)))
```
Do you need any assistance with anything else related to coding or algorithms?