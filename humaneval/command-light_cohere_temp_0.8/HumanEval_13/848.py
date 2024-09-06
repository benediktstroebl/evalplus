```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer")
    return max(x for x in range(1, min(a, b) + 1) if not a % x and not b % x)

# Unit tests
def test GreatestCommonDivisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5

if __name__ == "__main__":
    test GreatestCommonDivisor()
    print("Unit tests passed!")
```