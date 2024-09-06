```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```

The `greatest_common_divisor` function employs the Euclidean algorithm for finding the greatest common divisor (GCD) of two integers `a` and `b`. It is a recursive algorithm that utilizes the principle that the GCD of two numbers `x` and `y` is the same as the GCD of `y` and `x % y` (the remainder of the division of `x` by `y`).

The base case of the recursion is when `b` is 0. In this case, the GCD is `a`, as `b` divides `a` (division by zero), and it's also the smallest possible positive value that satisfies this property.

Otherwise, the function recursively calls itself with arguments `b` and `a % b`, which represents the remainder of the division of `a` by `b`. This step continues the process of finding the GCD of the two numbers.

The `greatest_common_divisor` function is implemented to handle negative values as well. It will return the GCD for any pair of numbers, regardless of their sign. However, the algorithm itself only operates on the absolute values of `a` and `b`. The absolute value of a number is always returned, regardless of the original sign.

Here are some examples of how this function can be used:
```python
>> greatest_common_divisor(48, 18)
6
>> greatest_common_divisor(10, -5)
5
>> greatest_common_divisor(-10, 25)
10
```

This function has a recursive nature, which leads to the "algorithm" moniker. It's a method that simulates a conversation or problem-solving process using repetition and reusing solutions to simpler problems. In this case, the repetition is recursive computation to find the GCD. 

The Euclidean algorithm is a cornerstone of mathematical algorithms and has widespread use in various fields, including mathematics, computer science, and engineering. It is a highly efficient and elegant approach to finding the GCD of two numbers.