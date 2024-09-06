```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero")
    return max(divisor(a) ,divisor(b))

def divisor(x: int) -> int:
    i = 1
    while x > 0:
        x //= i
        i += 1
    return i
```