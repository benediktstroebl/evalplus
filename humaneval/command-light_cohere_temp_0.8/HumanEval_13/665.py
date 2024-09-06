```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return max(d for d in range(1, min(a, b)) + 1 if a % d == 0 and b % d == 0)
```