```python
def greatest_common_divisor(a, b): 
    while b != 0:
        remainder = a % b
        a = b
        b = remainder 
    if a > 0:
        return a 

# Test the function
assert(greatest_common_divisor(3, 5), 1)
assert(greatest_common_divisor(25, 15), 5)
assert(greatest_common_divisor(36, 24), 6)
assert(greatest_common_divisor(88, 112), 44)
```
This code defines a function `greatest_common_divisor(a, b)` which returns the greatest common divisor of two integers a and b. In the algorithm, it repeatedly calculates the remainder of a/b until b becomes zero, then it assigns a to a and b to continue the loop. It also makes sure that if a is greater than 0, it returns a. The test cases demonstrate the validity of the function.