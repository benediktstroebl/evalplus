```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This GCD algorithm is a recursive variation of the Euclidean algorithm for computing the GCD. It makes use of the property that the GCD of two numbers `x` and `y` is the same as the GCD of `y` and `x % y`. With each recursive call, the smaller number is used as the second argument to improve efficiency. 

The algorithm terminates when the second argument becomes zero, at which point the first argument is the GCD.