Here is a Python script with a self-contained function that solves the problem of finding the greatest common divisor of two integers a and b:
```python
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def test_gcd():
    assert gcd(3, 5) == 1
    assert gcd(25, 15) == 5
```
This script defines a function gcd that calculates the greatest common divisor of two integers a and b using the Euclidean algorithm. The test_gcd function verifies the expected behavior of the gcd function with test cases.