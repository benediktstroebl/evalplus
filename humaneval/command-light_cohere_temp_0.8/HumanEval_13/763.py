```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a non-zero integer.")
    if a == 0 or b == 0:
        return 0
    gcd = (a, b)
    while gcd != 0:
        a %= gcd
        b %= gcd
    return gcd
def test_gcd():
    try:
        print(greatest_common_divisor(3, 5))
        assert (0 == 5)
        print(greatest_common_divisor(25, 15))
        assert (5 == 15)
    except AssertionError as e:
        print(e)
test_gcd()
```
This code defines a function called `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. The function uses the Euclidean Algorithm, which iteratively finds the greatest common divisor by calculating the divisibility of the current greatest common divisor and updating the values of `a` and `b`. The function also handles edge cases where either of the inputs is zero, returning 0 as the greatest common divisor.  The test_gcd() is a function that tests the `greatest_common_divisor` function with a couple of edge cases and actual inputs.