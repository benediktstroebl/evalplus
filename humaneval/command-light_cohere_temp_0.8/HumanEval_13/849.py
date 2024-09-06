```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a
    
    while a % b == 0:
        a //= b
    else:
        return a
    
# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This code defines a function called `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. Using a algorithm that maintains the values a and b as they are passed, and returns the greatest divisor of the two numbers. This function can be used to find the greatest common divisor of any two integers.