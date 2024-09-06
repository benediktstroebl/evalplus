```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be provided")
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both numbers must be integers")
    if a == 0:
        return 0
    if b == 0:
        return 0
    
    # Check for divisibility by a power of 2 until the square root of b
    while a != 0 and b != 0 and a % b == 0:
        a = a // b
    while a != 0 and b != 0 and a % b == 0:
        b = b // a
    return min(a, b)
```