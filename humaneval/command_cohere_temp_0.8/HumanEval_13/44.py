```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This approach uses Euclidean Algorithm to find the greatest common divisor. The algorithm repeatedly finds the remainder of the division of the larger number by the smaller number. 
The operation `b % a` finds the remainder of the division of `b` by `a`.
In each iteration, the smaller number is used as the dividend, and the remainder becomes the new dividend. 

The loop continues until the dividend is 0, and the divisor is the greatest common divisor of the two numbers.

The algorithm is more efficient when the divisors of the larger number are considered, hence the case `if a == 0`: to handle this scenario.