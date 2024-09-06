```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if all(n % dd == 0 for dd in range(1, n+1)))) or_match
```
Do you need any other code assistance?