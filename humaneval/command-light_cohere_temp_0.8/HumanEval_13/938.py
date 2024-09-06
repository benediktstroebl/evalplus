```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a

    while b > 0:
        a, b = b, a % b

    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(7, 21)))  # Output: 7
print(greatest_common_divisor(13, 15)))  # Output: 3 (correct)
 ``` 
This script defines a function `greatest_common_divisor` that calculates the greatest common divisor of two integers a and b. It employs a simple algorithm that iterates from b down to a smaller value, repeatedly dividing by the remainder until a zero value is reached.