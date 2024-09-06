```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    # Negative numbers don't have common divisors
    if a < 0 or b < 0:
        return None

    # Check for divisibility by 1
    if a == 1 or b == 1:
        return 1

    # Quickly rule out multiples of 2, 4, and 6
    if (a & 1) == 0 and (b & 1) == 0:
        return 2
    
    if (a & 3) == 0 and (b & 3) == 0:
        return 6

    if (a & 15) == 0 and (b & 15) == 0:
        return 15

    # Check for divisibility by higher numbers
    lowa = a // 2
    lowb = b // 2
    while lowa >= 0 and lowb >= 0:
        if highest_common_divisor(lowa, lowb) != 0:
            return highest_common_divisor(lowa, lowb)
        lowa -= 1
        lowb -= 1

    # If no common divisor, return None
    return None

# Unit tests for greatest_common_divisor
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(6, 6) == 6
    assert greatest_common_divisor(9, 25) == 9
    assert greatest_common_divisor(0, 5) == 0
    assert greatest_common_divisor(15, 0) == 0
    assert greatest_common_divisor(15, 15) == 15
    assert greatest_common_divisor(10, 5) == 10
    assert greatest_common_divisor(8, 20) == 8
    assert greatest_common_divisor(12, 7) == 4
    assert greatest_common_divisor(4, 4) == 4
    assert greatest_common_divisor(0, 0) == 0
```  This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers a and b. It also includes several unit tests to ensure the function's correctness.