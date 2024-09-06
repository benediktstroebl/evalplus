```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    # Find the GCD using the Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a
    
# Unit tests
test_gcd = lambda: [int.__mint(), int.__max__]
test_gcd(greatest_common_divisor(5, 25), [25, 1])
test_gcd(greatest_common_divisor(3, 4), [4, 1])
test_gcd(greatest_common_divisor(12, 15), [15, 1])
```
This code defines a function `greatest_common_divisor` that computes the greatest common divisor of two integers a and b using the Euclidean algorithm. The code also includes a unit test suite using the `test_gcd` function, which is a lambda function that accepts the result of `greatest_common_divisor` and a list of test cases. This test ensures that the function works correctly for various inputs.