```python
def greatest_common_divisor(a, b): 
    while b != 0: 
        a, b = b, a % b 
    return a

# Test case:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```
This code defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. It iteratively seeks the greatest common divisor by modifying `a` and `b` in a loop until `b` becomes zero, at which point the GCD is found and returned. The code also includes test cases that verify the function's correctness.