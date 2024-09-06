```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the numbers is required.")
    if a == 0 or b == 0:
        raise ValueError("Common divisor requires positive numbers.")
    return max(a, b) // gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Unit tests
test_gcd = lambda: [
    assert gcd(5, 10) == 5
    assert gcd(2, 4) == 2
    assert gcd(0, 0) == 0
    assert gcd(10, -5) == 0
    assert gcd(-10, 5) == 0
    assert gcd(15, 25) == 5

# Run the tests
test_gcd()
```
This code provides a self-contained function and tests for finding the greatest common divisor of two numbers. It includes checks for valid inputs and raises appropriate error messages if the inputs are invalid or zero. It also provides a specific input and expected output values.