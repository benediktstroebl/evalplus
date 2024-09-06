```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    # Find the largest divisor of smaller number
    i = max(a, b)
    while(i % a == 0 or i % b == 0):
        i += 1

    # Calculate the greatest common divisor
    gcd = i

    # Check if the divisor is equal to b
    if a == b:
        gcd = b

    return gcd
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(10, 50) == 5
    assert greatest_common_divisor(100, 25) == 25
    assert greatest_common_divisor(15, 250) == 125
    assert greatest_common_divisor(5, 5) == 5
```