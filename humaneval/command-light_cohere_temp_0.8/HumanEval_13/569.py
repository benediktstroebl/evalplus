```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    while a != 0 and b != 0 and a % b == 0:
        a = b
    return min(a, b)

# Test the function
def test GreatestCommonDivisor():
    a = 25
    b = 15
    assert greatest_common_divisor(a, b) == 5
    assert greatest_common_divisor(15, a) == 5

# Test another case
def test AnotherCase():
    a = 3
    b = 5
    assert greatest_common_divisor(a, b) == 1

test GreatestCommonDivisor()
test AnotherCase()
 ```