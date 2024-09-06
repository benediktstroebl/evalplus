```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    # Use Euclid's Algorithm
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

# Unit tests
test_gcd = typing.Union("int", "a", "b")
test_gcd(0, 5)  # Should return 0
test_gcd(5, 0)  # Should return 0
test_gcd(5, 5)  # Should return 1
test_gcd(15, 15)  # Should return 1
test_gcd(30, 15)  # Should return 5
test_gcd(25, 25)  # Should return 5
```