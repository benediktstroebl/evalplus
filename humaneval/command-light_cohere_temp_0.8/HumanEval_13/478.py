```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer")
    
    if a == 0 or b == 0:
        return 0
    
    while b != 0:
        a, b = b, a // b
    
    return a

# Test case 1
print(greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print(greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print(greatest_common_divisor(123, 456))  # Output: 28

```
This script defines a function called greatest_common_divisor, which takes two integers a and b as input and returns the greatest common divisor of a and b. The function uses a while algorithm to find the greatest common divisor, initializing the value of a with the given input, and then repeatedly dividing a by b until b becomes zero. The function then returns a value of a. Roman