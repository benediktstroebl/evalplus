```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is required")
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Input must be integers")
    if a == 0:
        return 0
    if b == 0:
        return 0

    # Compute GCD using the Euclidean algorithm
    while a != 0:
        b, a = a % b, a

    return b

# Unit tests
def test GreatestCommonDivisor():
    a = 3
    b = 5
    assert greatest_common_divisor(a, b) == 1
    a = 25
    b = 15
    assert greatest_common_divisor(a, b) == 5

if __name__ == "__main__":
    test GreatestCommonDivisor()
    print("Tests passed")
```