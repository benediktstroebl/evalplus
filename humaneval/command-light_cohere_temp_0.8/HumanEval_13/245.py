```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return greatest_common_divisor(b, a)
    return max(a % b for b in range(1, min(a, b)+1))
```