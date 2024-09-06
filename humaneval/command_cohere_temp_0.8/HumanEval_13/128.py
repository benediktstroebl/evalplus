```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This algorithm works by the Euclidean algorithm concept, which states that the gcd of two numbers `a` and `b` is the same as the gcd of `b%a` and `a`. In the case where `a` is 0, it returns `b` as there is no common divisor other than `b` itself. You can check the correctness by calling the function with the provided test cases. 
For example: 
```python
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
``` 
This should return the gcd of the given numbers in both cases, which is `1` and `5`, respectively.