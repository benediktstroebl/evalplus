Here is a self-contained Python script that solves the problem of finding the greatest common divisor of two integers a and b:
```python
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def test_gcd():
    assert gcd(3, 5) == 1
    assert gcd(25, 15) == 5
```

The gcd function uses the Euclidean algorithm to find the greatest common divisor. It works by dividing the maximum of the two numbers, which always results in the greater number becoming zero, and the smaller one remaining.

The test_gcd function contains several assertions that check if the gcd function is correct. The assertions are used to test the correctness of the function by passing different inputs and checking if the resulting gcd values are equal to the expected values.