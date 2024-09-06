```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs is zero.")
    return max(a, b) // gcd(a, b)

# Unit tests
def test GreatestCommonDivisor():
    try:
        a = 25
        b = 15
        assert greatest_common_divisor(a, b) == 5
        assert greatest_common_divisor(15, 25) == 5
    except Exception as e:
        print(f"Error occurred: {e}")
        assert False
```
This script defines a function `greatest_common_divisor` that computes the greatest common divisor of two numbers. It also includes a test function with a set of tests, ensuring the correctness of the `greatest_common_divisor` function.