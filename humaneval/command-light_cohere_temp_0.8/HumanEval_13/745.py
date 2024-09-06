```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    if a == 0:
        return 0
    if b == 0:
        return 0

    # Calculate gcd using the Euclidean algorithm
    while a != 0 and b != 0:
        a, b = b, a % b

    return b

# Unit tests
test_gcd = lambda: assert greatest_common_divisor(3, 5) == 1
test_gcd_zero = lambda: assert greatest_common_divisor(5, 0) == 0
test_divisor_zero = lambda: assert greatest_common_divisor(10, 0) == 0
test_large_numbers = lambda: assert greatest_common_divisor(25, 15) == 5
test_invalid_inputs = lambda: assert_Raises(ValueError, greatest_common_divisor, [5, "hello"]))
```