```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")

    # Calculate GCD using the Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

    # Test cases
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(-5, -7) == 1
    assert greatest_common_divisor(0, 5) == 0
    assert greatest_common_divisor(10, 200) == 10
    assert greatest_common_divisor(1234, 4321) == 4321
```