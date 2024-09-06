```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    if a == b:
        return a
    
    # Find the GCD using the Euclidean algorithm
    gcd = a
    while b != 0:
        a, b = b, a % b
    
    return gcd

# Unit tests
def test_greatest_common_divisor():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
```
This code defines a function greatest_common_divisor that calculates the greatest common divisor of two numbers a and b. Using Euclidean algorithm, this function efficiently determines the GCD, handling cases where the input is zero or equal. The unit tests afterward verify the necessary input combinations.