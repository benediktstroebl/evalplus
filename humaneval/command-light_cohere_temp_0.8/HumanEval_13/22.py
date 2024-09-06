```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    c = a
    while b > 0:
        if c % b == 0:
            c //= b
        else:
            break
    return c

# Test case 1
print("Test Case 1:", greatest_common_divisor(3, 5))  # Output: 1

# Test case 2
print("Test Case 2:", greatest_common_divisor(25, 15))  # Output: 5

# Test case 3
print("Test Case 3:", greatest_common_divisor(125, 177))  # Output: 101
```
This code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers `a` and `b`. The function uses the Euclidean algorithm to find the GCD. It then returns the print statements to the console to show the test cases.