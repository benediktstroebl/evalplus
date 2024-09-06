```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers should be greater than zero")
    return math.sqrt(max(a, b))
 
# Unit tests
test_gcd = [
    assert greatest_common_divisor(3, 5) == 1, "Failed: GCD(3, 5) = 1"
    assert greatest_common_divisor(25, 15) == 5, "Failed: GCD(25, 15) = 5"
]
```