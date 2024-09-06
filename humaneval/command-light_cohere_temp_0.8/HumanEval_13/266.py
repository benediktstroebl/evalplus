```python
def greatest_common_divisor(a, b): 
    while b != 0: 
        a,b = b, a % b 
    return a

# Test cases
print( greatest_common_divisor(3, 5) )  # Output: 1
print( greatest_common_divisor(25, 15) )  # Output: 5
``` 
This script defines a function greatest_common_divisor that calculates the greatest common divisor of two numbers a and b. It uses the dry loop and modulus operator to achieve this. 

The test cases ensure that the function correctly calculates the GCD of the given numbers. 

This is a self-contained Python script that contains the solution to the problem and passes all test cases.