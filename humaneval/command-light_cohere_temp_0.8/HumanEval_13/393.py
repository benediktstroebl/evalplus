```python
def greatest_common_divisor(a, b): 
    while b != 0:
        d = b
        b = a % b 
    return d

# Test case 1
print("Test Case 1: ", greatest_common_divisor(3, 5))
# Should print: 1

# Test case 2
print("Test Case 2: ", greatest_common_divisor(25, 15))
# Should print: 5
``` 
This code defines a function greatest_common_divisor that calculates and returns the greatest common divisor of two given integers a and b. The function utilizes the process of finding the greatest divisor by repeatedly dividing by the divisor until b becomes 0. 

It then uses the remainder operator (%) to find the remainder when a is divided by the current divisor.