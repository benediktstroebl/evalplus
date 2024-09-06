```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Recursive approach is quite elegant and uses less code to implement. It is also easier to understand and conceptualize. However, recursion incurs constant function call overhead, which can be substantial for large inputs, and leads to stacked loop overhead.

The gcd function checks if the b value is 0, and if so, returns a immediately, indicating that a is the gcd of the two numbers. Otherwise, it repeats the process by calling gcd again, this time with the arguments in the order b and a % b. The modulo operator is used to repeatedly eliminate b from the calculation until it is zero, at which point the remaining number is the gcd of a and b. 

The function employs tail recursion, which is optimized in Python. The recursion stack size is O(log(min(a,b))) and the constant stack overhead is generally negligible.