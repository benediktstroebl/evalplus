```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    # Find the greatest divisor of a and b
    gcd = math.gcd(a, b)
    return gcd

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(7, 12) == 4
    assert greatest_common_divisor(9, 56) == 9
    assert greatest_common_divisor(59, 120) == 21
    assert greatest_common_divisor(8, 45) == 45
    assert greatest_common_divisor(21, 105) == 7
    assert greatest_common_divisor(88, 181) == 44

    print("GreatestCommonDivisor unit tests passed")
``` 
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of 2 numbers passed as arguments. The function includes input validation to handle cases where either of the input numbers are 0, and returns 0 in such cases. The function then uses the mathematical function `math.gcd` to calculate the gcd of the 2 input numbers, and finally returns the result.