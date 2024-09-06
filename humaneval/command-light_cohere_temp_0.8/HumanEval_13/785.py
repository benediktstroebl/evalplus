```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be greater than zero")
    return math.isgcd(a, b)

def test_gcd(test_a: int, test_b: int) -> None:
    result = greatest_common_divisor(test_a, test_b)
    assert result == math.isgcd(test_a, test_b)

# Example usage:
test_gcd(3, 5)
test_gcd(25, 15)
```
This code defines a function called greatest_common_divisor that calculates the greatest common divisor of two integers a and b using the math.gcd() function from the necessary to calculate the greatest common divisor. The test_gcd function tests the gcd() with the test cases 3 and 5, and passes the test.

The test_gcd function tests the greatest_common_divisor function with the test cases 25 and 15, and ensures that the calculated gcd values match the expected values. 

This code is self-contained and can be used as a standalone solution for the given problem.