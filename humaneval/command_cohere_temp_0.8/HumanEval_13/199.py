```python
def greatest_common_divisor(a, b) -> int:
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```
This script defines a recursive function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns the greatest common divisor of the two integers. The base case of the recursion is if `a` or `b` is zero, in which case the other number is returned. Otherwise, the function recursively returns the gcd(b%a, a). This is a common approach to finding the gcd using modular arithmetic. 

Here is an example usage of the function:
```python
print(greatest_common_divisor(10, 15))  # gcd(10, 15) = 5
print(greatest_common_divisor(6, 18))  # gcd(6, 18) = 6
print(greatest_common_divisor(30, 10))  # gcd(30, 10) = 10
``` 

This will output:
```bash
5
6
10
``` 
as the gcd of the respective pairs of numbers.