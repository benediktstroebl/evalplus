```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    return max(divisor(a) ,divisor(b))

def divisor(x: int) -> int:
    if x == 0:
        return 0
    return x
```