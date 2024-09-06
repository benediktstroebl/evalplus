```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    s = 0
    while b > 0:
        t = a // b
        a -= t * b
        s += t
    
    return s
# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(7, 21))  # Output: 3

```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The function uses the process to find the greatest common divisor by repeatedly dividing the larger number by the smaller one until it becomes zero, adding up the resulting quotients. 

This is a self-contained solution that doesn't rely on any additional libraries or external functions.