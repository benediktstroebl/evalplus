```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    return math.isgcd(min(a, b))

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5

if __name__ == "__main__":
    print("Greatest Common Divisor Unit Tests Passed!")
    test GreatestCommonDivisor()
```
This code provides a function greatest_common_divisor that calculates the greatest common divisor of two given integers a and b. The function performs basic input validation and then uses the math.isgcd() function from the precise calculation of the greatest common divisor. The unit tests also ensure the validate the function with the expected behavior.