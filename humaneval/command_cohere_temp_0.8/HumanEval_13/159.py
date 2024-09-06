```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a function called `greatest_common_divisor` that takes two integers a and b as input and returns the greatest common divisor of the two numbers. 

The base case of the recursion is b == 0. In that case, the function returns a since all divisors of a will also be divisors of the other number b.

If b is not zero, the function recursively calls itself, passing the arguments b and a % b. The modulus % operator is used to compute the remainder of a divided by b. This remainder will have a common divisor with b, and this common divisor will also be a divisor of a. By repeatedly calling the function recursively while updating the arguments, the function converges towards the greatest common divisor of a and b.