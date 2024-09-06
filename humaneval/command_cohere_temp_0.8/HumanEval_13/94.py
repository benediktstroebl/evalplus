```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This GCD algorithm is a recursive variation of the Euclidean algorithm for computing the GCD. It exploits the property that the GCD of two integers `a` and `b` is the same as the GCD of `b` and `a % b`. Here, the modulo operator `%` ensures that the remainder of the division of `a` by `b` is computed, giving the unique positive value in the set `{b, a % b, a}`. 

It is called recursively until the 'b' value is reduced to zero. At this point, the value of `a` will be the GCD of the original `a` and `b`. 

The algorithm is not considered efficient for large numbers since it uses recursion, but it's a straightforward implementation of the Euclidean algorithm. 

This algorithm is generally efficient for practical purposes, but it has a worst-case time complexity of O(n). This worst-case scenario happens when the inputs are two consecutive Fibonacci numbers, and the recursion tree is the most extensive. Despite this worst-case scenario, the algorithm is widely used due to its simplicity and speed for most real-world problems.