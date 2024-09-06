```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The `greatest_common_divisor` function employs the Euclidean algorithm for computing the GCD of two integers `a` and `b`. It is a recursive algorithm that employs the principle that the GCD of two numbers `x` and `y` is the same as the GCD of `y` and `x % y`. If the second integer `b` is zero, the function returns the first integer `a` as the GCD of `a` and `b` as according to the Euclidean algorithm. 

Here is an example usage of the function:
```python
>> greatest_common_divisor(12, 18)
6
```

The result is the greatest common divisor of 12 and 18, which is 6. 

This algorithm's time complexity is `O(log(min(a, b)))`, which makes it an efficient method for calculating the GCD of two integers.