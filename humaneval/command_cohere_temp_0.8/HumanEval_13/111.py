```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The algorithm is a recursive variation of the Euclidean algorithm for computing the greatest common divisor. It exploits the property that the GCD of two integers `a` and `b` is the same as the GCD of `b` and `a % b`. 

It's called recursively until `b` is zero and then it returns `a`, which is the GCD. This algorithm is efficient because the Euclidean algorithm subtracts smaller values from `b` at each step, resulting in fewer divisions and arithmetic operations. 

The base case of the recursion is when `b` reaches zero, at which point the function returns `a`, as `a` is then the GCD of the two numbers. 

This algorithm's time complexity is O(log(min(a, b))), which makes it an efficient method for calculating the GCD of two integers.