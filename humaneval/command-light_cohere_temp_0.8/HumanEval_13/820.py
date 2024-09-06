```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero.")
    return math.floor(math.sqrt(math.pow(a,b) / math.sqrt(a)) + 1)
```