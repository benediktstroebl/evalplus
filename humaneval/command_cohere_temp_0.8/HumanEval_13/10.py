```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The `greatest_common_divisor` function employs recursion to find the greatest common divisor (GCD) of two integers `a` and `b`. It utilizes the Euclidean algorithm to efficiently compute the GCD. 

The base case of the recursion occurs when `b` is zero, in which case the GCD is `a`. Otherwise, the function recursively calls itself with the arguments `b` and `a % b`, which represents the remainder of the division of `a` by `b`. This choice of `b` and the remainder ensures that the recursion progresses towards the correct solution.

The recursive nature of the algorithm allows it to gracefully handle larger integers by effectively reducing the problem size with each recursion step. As a result, the time complexity of the algorithm is linearly proportional to the smaller of the two input integers, `a` and `b`.