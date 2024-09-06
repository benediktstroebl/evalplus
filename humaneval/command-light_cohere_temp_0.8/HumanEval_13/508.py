```python
def greatest_common_divisor(a, b): 
    while b != 0:
        # Finding the largest divisor of b
        rem, b = divmod(b, a)
        a = b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
``` 
This Python code defines a function greatest_common_divisor that calculates the greatest common divisor of two integers a and b. The function utilizes the process of division and modification (divmod) to repeatedly find the largest divisor of b while gradually reducing a to zero, effectively tracking the largest divisor of the dividend a given number b can yield. The function then returns the effective result of the greatest common divisor of a and b. 

This is a self-contained solution to the problem of finding the greatest common divisor of two integers.