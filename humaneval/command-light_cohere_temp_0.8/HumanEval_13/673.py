Here is a self-contained Python script with a function that solves the problem of finding the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("One or both input numbers is empty")
    return max(a, b) // gcd(a, b)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

# Unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(9, 25) == 1
    assert greatest_common_divisor(13, 4) == 13
    assert greatest_common_divisor(10, 50) == 10
```