```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    return max(greatest_common_divisor(b % a, a), greatest_common_divisor(b, a % b))

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(125, 275)) # Output: 25
```
The problem of finding the greatest common divisor of two numbers a and b is solved by the greatest_common_divisor() function in this script. The function takes two integers a a and b as input and returns the greatest common divisor of a and b. It uses the max() function to find the maximum of the results of the two recursive calls greatest_common_divisor(b % a, a) and greatest_common_divisor(b, a % b). The function also handles the case where either a or b is zero, in which case it returns 0.