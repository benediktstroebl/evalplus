```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not n % d), -1)
```
Do you need help with anything else with Python scripts and functions?