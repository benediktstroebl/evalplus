```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```

The `greatest_common_divisor` function uses recursion to find the greatest common divisor of two integers `a` and `b`. It is advised to use the same naming convention as the provided function name to improve code readability and maintainability. 

If a is 0, the base case of the recursion, b is returned to avoid an infinite loop. Otherwise, the function recursively calls itself with the arguments `b%a` and `a`, which represents the remainder of b divided by a and a respectively. This process continues until a reaches 0, at which point the recursion ends and the current value of b is returned as the greatest common divisor. 

Please note that this approach leverages Euclid's Algorithm to find the GCD, which is widely used in computer science and has a time complexity of O(log(min(a,b))).