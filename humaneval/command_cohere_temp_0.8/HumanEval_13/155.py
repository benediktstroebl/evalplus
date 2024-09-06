```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a function `greatest_common_divisor` that takes two integers `a` and `b` as arguments and returns the greatest common divisor of the two numbers. 

The base case of the recursion is b == 0, in which case the function returns a. The recursive case calculates the GCD of b and the remainder of a divided by b. This continues until b is 0, at which point the remainder is the GCD of the original two numbers. 

The script captures the idea of traversing the Euclidean Algorithm from the given example and is a clear and efficient approach for calculating the GCD. 

This function can be easily incorporated into larger code bases. Feel free to modify the documentation for readability. Let me know if I can assist with any other questions!