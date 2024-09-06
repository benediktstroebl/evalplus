```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max(divisor(a) ,divisor(b))

def divisor(x: int) -> int:
    if x == 0:
        return 1
    return x
```