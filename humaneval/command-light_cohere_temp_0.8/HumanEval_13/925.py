```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Incorrect input values.
    return math.max(a gcd(a, b), 0)

def gcd(a: int, b: int) -> int:
    while not b:
        a, b = b, a
    return a

def test_gcd():
    a = 2
    b = 3
    assert greatest_common_divisor(a, b) == 1
    a = 25
    b = 15
    assert greatest_common_divisor(a, b) == 5
```