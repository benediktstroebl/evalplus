```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a recursive function `greatest_common_divisor` that calculates the greatest common divisor (GCD) of two given integers `a` and `b` using the Euclidean algorithm. If `b` is 0, it returns `a` since `a` is the GCD of any number and 0. Otherwise, it recursively calls itself with the arguments `b` and `a % b`, which represents the remainder of the division of `a` by `b`. The function continues this process until `b` becomes 0, at which point it returns the original value of `a`, which is the GCD of the initial `a` and `b`. This algorithm is efficient due to the recursive nature of its divisibility tests. 

Here is an example usage of the function:
```python
print(greatest_common_divisor(48,36))
```
The output will be:
```
12
``` 

This demonstrates finding the GCD of 48 and 36, which is 12.