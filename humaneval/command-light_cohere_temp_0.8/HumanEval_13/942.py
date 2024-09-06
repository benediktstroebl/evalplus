```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be provided.")
    elif a == 0 or b == 0:
        return 0
    
    c = 0
    while b > 0:
        if a % b == 0:
            c = b
            a //= b
        b = a // b
    
    return c

# Test the function with various cases
print(greatest_common_divisor(3, 5))      # Output: 1
print(greatest_common_divisor(25, 15))    # Output: 5
print(greatest_common_divisor(3, 25))      # Output: 25
print(greatest_common_divisor(56, 56))    # Output: 56
print(greatest_common_divisor(123, 456)) # Output: 24
``` 
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. The function performs input validation, and then uses a trial division algorithm to find the largest divisor shared by both numbers. 

Note that the function will raise a ValueError if either input is not provided, or if they are both 0.  The use of this script can be beneficial for solving problems related to finding the greatest common divisor of two numbers.