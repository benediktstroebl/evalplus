```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Python script defines a function called `greatest_common_divisor`. It takes in two integers, `a` and `b`, as arguments. The function calculates and returns the greatest common divisor (GCD) of these two integers. 

The GCD of two numbers `a` and `b` is the largest positive integer that evenly divides both `a` and `b`. For example, the GCD of 8 and 12 is 4, since it's the largest number that divides both 8 and 12 without leaving a remainder.

This function uses a recursive approach to finding the GCD. It starts by checking if `b` is 0. If `b` is 0, it means that `a` is the GCD, so the function returns `a`. If `b` is not 0, the function calls itself recursively, passing `b` and `a % b` as arguments. This process continues until `b` becomes 0, at which point the recursion unwinds and the GCD is found.

This approach leverages the convenient mathematical property that the GCD of two numbers `a` and `b` is the same as the GCD of `b` and `a % b`. Each recursive call trims down the larger number (`b`) by taking its remainder with respect to the smaller number (`a`). Eventually, when `b` becomes 0, the remainder (`a % b`) becomes the GCD of the original two numbers.

Overall, this Python function efficiently calculates the GCD of two integers `a` and `b` using a recursive approach.