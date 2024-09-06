```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This straightforward function uses the Euclidean algorithm for computing the GCD. It exploits the fact that the modulo operation retains the same remainder when the divisor is substituted with the dividend's negative. This approach minimizes the time complexity to O(log(min(a, b))). 

Here's a test suite to ensure it meets the specified problem:
```python
def test_gcd():
    """
    Test the greatest_common_divisor function.
    """
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 30) == 30
    assert greatest_common_divisor(1, 1) == 1
    assert greatest_common_divisor(10, 5) == 5
    assert greatest_common_divisor(7, -11) == 1
test_gcd()
```
The test suite consists of various scenarios, including positive and negative integers, zeros, and an input with a denominator equal to zero.