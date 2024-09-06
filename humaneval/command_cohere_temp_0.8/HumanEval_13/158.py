```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This algorithm works by the Euclidean algorithm for computing the GCD. The algorithm repeatedly divides the larger number by the smaller number (removing the smaller number from the larger number). Theoretically, the process continues until the smaller number becomes 0. The biggest number that can divide both a and b without leaving a remainder is the GCD. When the smaller number becomes 0, the larger number is the GCD of the two numbers. If a is 0, the algorithm stops and b is returned since the GCD of 0 and any number is that number. 

Here is a test suite for the function:
```python
def test_gcd():
    """ Tests the greatest_common_divisor function """
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(0, 30) == 30
    assert greatest_common_divisor(10, 0) == 0
    assert greatest_common_divisor(61, 43) == 7
    assert greatest_common_divisor(-61, -43) == 7
``` 

Running the test suite will ensure that the greatest_common_divisor function works as expected. 
```test_gcd()
```