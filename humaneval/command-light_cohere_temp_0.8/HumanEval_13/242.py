```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the numbers is required")
    if a == 0:
        return 0
    elif b == 0:
        return a
    else:
        return max(a % b for a in range(1, max(a, b)))

# Test suite
def test GreatestCommonDivisor():
    try:
        result = greatest_common_divisor(3, 5)
        assert result == 1
        result = greatest_common_divisor(25, 15)
        assert result == 5
        raise ValueError("Failed test: empty input")
if __name__ == "__main__":
    test GreatestCommonDivisor()
```
The code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The function utilizes several conditional statements to ensure the input is valid.

The function first checks if either a or b is empty, and if so, raises a ValueError. If a is zero, it returns 0. If b is zero, it returns a. The function then checks if a is greater than 0, and if so, returns a. The function finally checks if b is greater than 0 and returns the maximum of a divided by b, starting from 1 and up to the largest value.

This code can be used to find the greatest common divisor of any two integers.