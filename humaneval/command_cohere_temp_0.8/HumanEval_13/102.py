```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This Recursive approach for computing the GCD of two numbers is founded on the principle of exhaustion. The function repeats the process until the smaller number becomes zero. At this point, the larger number is returned as the GCD. This is efficient in terms of time and logic. 

The greatest common divisor of 12 and 8 is 4, which is computed by the following call:
```python
>>> greatest_common_divisor(12, 8)
4
```

The greatest common divisor of 25 and 15 is 5, which is computed by the following call:
```python
>>> greatest_common_divisor(25, 15)
5
```