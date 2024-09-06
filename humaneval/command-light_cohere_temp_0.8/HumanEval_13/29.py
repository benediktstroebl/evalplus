```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero.")
    elif a == b:
        return 0
    else:
        return max(a, b) // gcd(a, b)
 
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
 
# Unit tests
try:
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
except AssertionError as e:
    print(f"Error: {e}" )
```