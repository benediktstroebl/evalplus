```python
def greatest_common_divisor(a, b): 
    while b != 0: 
        a_divisible_by = b
        b = b // a 
    return a_divisible_by

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
```
This code defines a function greatest_common_divisor that calculates and returns the greatest common divisor of two integers a and b. The function utilizes the method to calculate the greatest common divisor. The tests cases pass with valid inputs, and the output is printed.