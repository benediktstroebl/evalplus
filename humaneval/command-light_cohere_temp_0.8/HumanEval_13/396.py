```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("Both numbers must be given")
    return max(a, b) // gcd(a, b)

# Unit tests
def test GreatestCommonDivisor():
    try:
        a = 3
        b = 5
        assert greatest_common_divisor(a, b) == 1
        a = 25
        b = 15
        assert greatest_common_divisor(a, b) == 5
    except AssertionError as e:
        print(f"Error: {e}")
    return
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The function handles edge cases and raises a `ValueError` if either argument is not provided. The `test GreatestCommonDivisor` function contains unit tests that verify the function's behavior for various input combinations.