```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a recursive function `greatest_common_divisor` that finds the greatest common divisor of two integers `a` and `b`. It utilizes the Euclidean algorithm to efficiently compute the GCD. If `b` is zero, it returns `a` since `a` is the GCD of any number and zero. Otherwise, it recursively calls itself with the arguments `b` and `a % b`, which represents the remainder of the division of `a` by `b`. 

The script is self-contained, meaning it does not rely on any external libraries or modules to execute. It is a standalone solution to the problem and can be executed independently. Additionally, the function is designed to be efficient, with a time complexity of O(log(min(a, b))).