```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This algorithm optimizes a recursive approach to computing the GCD using the Euclidean algorithm, which reduces the larger number by successive divisions until it becomes zero. The modulus operation efficiently approximates this reduction. 

Here is a test case to ensure the algorithm works as expected:
```python
def test_gcd():
    """ Tests the greatest_common_divisor function """
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 25) == 25
    assert greatest_common_divisor(10, 0) == 10
```