```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The `greatest_common_divisor` function employs recursion to find the greatest common divisor (GCD) of two integers `a` and `b`. It leverages the property that the GCD of two numbers `x` and `y` is the same as the GCD of `y` and `x % y`. If `b` is 0, it returns `a` as there is no divisor of infinity that is greater than `a`. 

Here is an example usage of the function that demonstrates the correctness of the algorithm:
```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
```
This function is not the most efficient approach, as it invokes recursion for every recursive call, resulting in redundant calculations. To optimize it, you can introduce memoization or use mathematical formulas like the Euclidean algorithm to find the GCD.