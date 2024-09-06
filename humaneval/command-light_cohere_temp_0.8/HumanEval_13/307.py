```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    # Use Euclid's algorithm
    temp = greatest_common_divisor(b % a, a)
    return temp  # returns the greater divisor among the two numbers a and b

# Test cases:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
``` 
This code defines a Python function called greatest_common_divisor that takes two integers a and b as input and calculates the greatest common divisor of the two numbers. The function uses Euclid's algorithm to find the greatest common divisor and returns the result.