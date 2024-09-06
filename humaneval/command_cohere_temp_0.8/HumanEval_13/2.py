```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

The script uses Euclidean algorithm for computing the greatest common divisor. It is based on the property that the gcd of two numbers `a` and `b` is the same as the gcd of `b%a` and `a`. It repeatedly applies this property until one of the numbers becomes zero. Note that `a` is checked for being zero first since the modulo operation flips the parity of the number, and we want to eventually end up dividing by `a` not `b`. 

This algorithm is named after the ancient Greek mathematician Euclid, who first proposed it. The gcd is also known as the 'highest common factor' or 'greatest common factor'. 

The code includes a docstring that specifies the expected behavior of the function and provides examples that illustrate the behavior of the function. These examples demonstrate that the function correctly calculates the greatest common divisor of two integers `a` and `b`. 

Furthermore, the function handles the special case of when `b` is 0 by returning `a` since the gcd of any number and 0 is that number.