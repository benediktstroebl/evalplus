```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n + 1) if not any(n % x == 0)) - 1)
```
Do you need assistance with anything else related to code readability, performance optimization, or other concepts?