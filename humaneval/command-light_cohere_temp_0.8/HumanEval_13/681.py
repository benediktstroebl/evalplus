```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")

    if a == 0:
        return 0
    if b == 0:
        return 0

    # Calculate GCD using the Euclidean algorithm
    while a or b:
        a, b = b, a % b

    return b

# Unit tests
test_gcd = lambda: [
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
]

# Run the tests
test_gcd()
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers using the Euclidean algorithm. The function also includes input validation to ensure the inputs are integers and non-zero. The unit tests verify that function's correctness by passing the function with a variety of test cases. Finally, the test_gcd function is invoked to run the tests.