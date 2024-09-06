```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    max_div = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            max_div = max(max_div, i)

    return max_div

# Test suite
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(7, 12) == 4
    assert greatest_common_divisor(0, 15) == 0
    assert greatest_common_divisor(50, 25) == 25
    assert greatest_common_divisor(48, 49) == 48
    assert greatest_common_divisor(9, 2) == 3
    assert greatest_common_divisor(0, 6) == 0
```  The function `greatest_common_divisor` takes two integers `a` and `b` as input, and returns the greatest common divisor of the two numbers. The function uses a testing and debugging tools, such as assertions, to ensure the function's correctness and output reliability.