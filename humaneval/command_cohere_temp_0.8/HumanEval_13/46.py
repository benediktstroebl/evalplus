```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```

The `greatest_common_divisor` function uses the Euclidean algorithm for computing the GCD. It refines the algorithm from earlier by immediately returning `a` if it is 0, since `b` will be the GCD in this case. This optimization further reduces the number of steps required to compute the GCD. 

This algorithm is known for its efficiency, as it reduces the problem size continuously with each step, resulting in relatively few steps required to determine the GCD of two numbers. 

The docstring includes example usage and expected output, which are helpful for developers to quickly understand how to use the function and confirm its behavior. 

This function can be called like any other Python function, and it will return the greatest common divisor of the two provided integers a and b. 

It is important to note that this function assumes that the input integers are not null. If either integer is null, the function may throw an error or return an unexpected value.