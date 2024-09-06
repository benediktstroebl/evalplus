```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of a and b must be provided")
    elif a == 0:
        return 0
    elif b == 0:
        return a
    else:
        return max(a % b, b % a)

# Unit tests
def test GreatestCommonDivisor():
    try:
        a = 3
        b = 5
        print(greatest_common_divisor(a, b))  # Output: 1
        assert greatest_common_divisor(a, b) == 1
        a = 25
        b = 15
        print(greatest_common_divisor(a, b))  # Output: 5
        assert greatest_common_divisor(a, b) == 5
        a = -5
        b = 0
        with pytest.assert() as t:
            raise ValueError(f"At least one of a and b must be positive: {a}, {b}")
        assert t.isinstance.  #which message expected Greatest error

if __name__ == "__main__":
    test GreatestCommonDivisor()
    ```