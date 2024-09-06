```python
def greatest_common_divisor(a, b): 
    while b != 0:
        if a % b == 0: 
            a_val = b 
            b = a // b 
        else: 
            a = b 
    return a

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers a and b. The function uses the process to repeatedly find the divisor of a until it becomes zero. The function then returns the maximum divisor.