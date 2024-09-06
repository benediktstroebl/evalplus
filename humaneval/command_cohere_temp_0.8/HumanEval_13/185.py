```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)
```
This recursive approach to finding the greatest common divisor leverages the property that `gcd(x, y) = gcd(y%x, x)` 

To better understand this approach, let's use an example:
```python
greatest_common_divisor(40, 56)
# greatest_common_divisor(56%40, 40)
# greatest_common_divisor(16, 40)
# greatest_common_divisor(40%16, 16)
# greatest_common_divisor(8, 16)
# greatest_common_divisor(16%8, 8)
# greatest_common_divisor(0, 8)
# 8
```

The initial call is `greatest_common_divisor(40, 56)` and then each subsequent line represents a recursive call to the function, the updated values of `a` and `b`, and the GCD so far `8` is the correct GCD of `40` and `56` and is produced by this sequence of recursive calls. 

This approach provides a clean and efficient solution to the problem. 

Let me know if I can provide further assistance!