```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    
    # To store the result
    gcd = 0
    
    while b != 0:
        a, b = b, a % b
    
    return gcd

# Unit tests
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5
assert greatest_common_divisor(16, 12) == 4
assert greatest_common_divisor(7, 49) == 7
assert greatest_common_divisor(56, 7) == 56
assert greatest_common_divisor(21, 441) == 441
```
This Python code defines a function called `greatest_common_divisor`, which calculates the greatest common divisor of two integers a and b. The function employs the method to find the GCD, initializing a variable gcd to store the result, and iteratively updating it with the divisor of b until b becomes zero. The function then returns the gcd. This code covers the also simple cases: where the inputs are either 0 or not, and handles other edge cases with unit tests.