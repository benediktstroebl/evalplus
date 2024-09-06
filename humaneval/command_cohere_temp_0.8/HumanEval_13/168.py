```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

The GCD function uses Euclidean algorithm for computing the GCD of two numbers. It is called recursively with arguments b%a and a, which ensures that each subsequent call returns a smaller value than the previous call for any non-zero values of a and b. The base case is when either a or b is 0, where the other number is returned as the GCD. 

This approach is efficient due to the property that it makes the coefficient smaller in each step, O(log(min(a,b))).

The above approach works for positive integers. For handling negative numbers, you can modify the function by transforming the inputs to positive before applying the above algorithm and then transforming the result back to the original sign.