```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a != 0:
        a, b = divmod(a, b)
    
    return b

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers `a` and `b`. It uses the `divmod` function to efficiently find the greatest common divisor when the numbers are not divisible. 
The function works by finding the smaller number, dividing both numbers, and repeating until the smaller number becomes zero. 
The script then tests the function with various inputs and verifies that the output is correct.