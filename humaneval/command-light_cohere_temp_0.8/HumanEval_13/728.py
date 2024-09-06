```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be greater than zero")
    return max(a, b) // int(math.isprime(max(a, b))) + 1 if max(a, b) > 1 else 1
```