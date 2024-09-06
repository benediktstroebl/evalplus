```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    if a == b:
        return a

    for divisor in range(1, len(factorize(a)) + 1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    return -1

# Testing
def test_greatest_common_divisor():
    a = 25
    b = 15

    assert greatest_common_divisor(a, b) == 5
```