```python
def greatest_common_divisor(a, b):
    """Return the greatest common divisor of two integers a and b."""
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive approach is quite common for calculating GCDs and utilizes the property that the GCD of two numbers `a` and `b` is the same as the GCD of `b%a` and `a`. 
The base case of this recursive approach is when `a` is 0, in which case it returns `b` as the GCD of the two numbers. 

Here's a basic test suite for this function: 
```python
def test_gcd():
    """Test the greatest_common_divisor function."""
    assert greatest_common_divisor(10, 15) == 5
    assert greatest_common_divisor(10, 0) == 10
    assert greatest_common_divisor(0, 100) == 100
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(3, 5) == 1
``` 
Running these test cases will assert that the `greatest_common_divisor` function behaves as expected.