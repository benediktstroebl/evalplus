```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a recursive function `greatest_common_divisor` that takes two integers `a` and `b` as inputs. It uses recursion to find the greatest common divisor (GCD) of the two numbers. 

The base case of the recursion is when `b` is 0. In this case, the GCD is `a`, as `b` divides `a` (assuming `a` is not 0). 

For non-zero values of `b`, the function recursively calls itself with the arguments `b` and `a % b`. This is done pursuant to the Euclidean algorithm, which states that the GCD of two numbers `a` and `b` is the same as the GCD of `b` and `a % b`. 

By repeatedly calling `greatest_common_divisor(b, a % b)` and using the base case for `b==0`, the function marches towards the GCD of the original `a` and `b`. 

The script provides a quick and efficient way to find the GCD of two integers.