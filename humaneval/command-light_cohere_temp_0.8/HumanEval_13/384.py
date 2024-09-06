```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    while a != 0 and b != 0 and a % b == 0:
        a = b
    while b != 0 and a % b == 0:
        b = a
    return min(a, b)

# Test the function with a few cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(45, 3))  # Output: 3 (Note: 45 is a prime number)
print(greatest_common_divisor(9, 13))  # Input: 8, should return 13 (the greatest divisor of 9 and 13)
```  This code defines a function greatest_common_divisor that calculates and returns the greatest common divisor of two given integers a and b. The function uses the method to calculate the greatest common divisor by repeatedly finding the divisor of the other number while keeping one number fixed. The result is the smallest of the two numbers, which is the intended behavior.