```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    while a > 0 and b > 0:
        if a % b == 0:
            a, b = a // b,
        else:
            a -= b
    return max(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
``` 
This script defines a function greatest_common_divisor that calculates the greatest common divisor of two given integers a and b. The function uses a iterative approach with conditional assignments to find the greatest divisor. The test cases validate the desired behavior of the function.