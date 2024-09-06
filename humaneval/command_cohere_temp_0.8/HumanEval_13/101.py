```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive algorithm is inspired by the Euclidean algorithm. It exploits the property that the gcd of two numbers `a` and `b` is equal to the gcd of `b` and `a % b`. The base case of the recursion is when `b` is 0, in which case it returns `a`, assuming `a` is not 0. 

Here is a test suite that can be used to validate the function:
```python
def test_gcd():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(1, 1) == 1
    assert greatest_common_divisor(51, 43) == 7
    assert greatest_common_divisor(0, 30) == 30
    assert greatest_common_divisor(10, 0) == 10
```