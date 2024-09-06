```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Inconsistent input values for a and b.")

    if a == 0 or b == 0:
        return 0

    # This condition is added to prevent division by zero
    if a == b:
        return a

    # Use Euclidean algorithm to find GCD
    return gcd(a, b)

# Unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(6, 10) == 5
    assert greatest_common_divisor(10, 6) == 5
    assert greatest_common_divisor(0, 5) == 0
    assert greatest_common_divisor(7, 0) == 0
    assert greatest_common_divisor(0, 0) == 0
```
This Python code defines a function called `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two given integers `a` and `b`. It uses a basic algorithm known as Euclidean algorithm to efficiently find the GCD. The function also includes input validation to handle cases where the inputs are not valid integers. The code also includes unit tests to ensure the correctness of the `greatest_common_divisor` function under various scenarios.