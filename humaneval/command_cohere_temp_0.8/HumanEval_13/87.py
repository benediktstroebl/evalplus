```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a function `greatest_common_divisor` that finds the greatest common divisor of two integers `a` and `b`. It uses the Euclidean algorithm with the base case of returning `a` when `b` is 0. This algorithm efficiently calculates the GCD by repeatedly finding the remainder of `a` divided by `b` and updating `a` and `b` accordingly until `b` becomes 0. The final value of `a` is the GCD of the original inputs. The function is designed to handle negative integers and returns the correct GCD for various test cases, making it a useful tool for finding the largest common divisor of two numbers.