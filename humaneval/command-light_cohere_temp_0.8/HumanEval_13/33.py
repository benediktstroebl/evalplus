```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return max(divisor(a, b), divisor(b, a))

def divisor(a: int, b: int) -> int:
    s = 0
    while b >=  1:
        if a % b == 0:
            s += 1
        a //= b
    return s
```