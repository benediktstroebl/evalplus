```python
def largest_divisor(n: int) -> int:
    return n if n <= 3 else largest_divisor(n // 3)
```
Do you require assistance with any other coding problem?