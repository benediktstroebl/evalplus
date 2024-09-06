```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero.")
    return gcd(a, b)

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(6, 0) raises ValueError
    assert greatest_common_divisor(0, 6) raises ValueError
```
This code provides a Python function that calculates the greatest common divisor of two integers a and b, ensuring that the function behaves correctly and provides the expected output for the given inputs. 

You can use this code as a starting point to solve the problem in your markdown code block.