```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The algorithm works by leveraging the fact that the greatest common divisor of two integers `a` and `b` is also the greatest common divisor of `b` and `a % b`. This is because any common divisor of `a` and `b` will also be a common divisor of `b` and `a % b`. The base case of the algorithm occurs when `b` is 0, since the greatest common divisor of `a` and 0 is `a`. 

This function is invoked with two integers a and b, and it returns the greatest common divisor of these two integers. To demonstrate the function is correct, it's passed tests corresponding to the specs you provided:
```
# Testing Function
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
>>> greatest_common_divisor(2, 10)
2
>>> greatest_common_divisor(0, 0)
0
``` 
As specified in the problem statement, the function returns the greatest common divisor of two integers `a` and `b`.