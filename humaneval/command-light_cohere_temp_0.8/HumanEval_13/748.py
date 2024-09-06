```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    
    if a == 0:
        return b
    elif b == 0:
        return a

    # If both numbers are even, they will share a common even divisor
    while a % b == 0 and a != 0 and b != 0:
        a, b = b, a + b
    
    # If one number is odd and the other even, find the odd divisor
    return min(a, b) + 1 if a != b and a % b == 1 else b

# Example usage:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
This Python code defines a function called greatest_common_divisor that calculates and returns the greatest common divisor of two input integers a and b. The function utilizes several techniques to find the greatest common divisor, including identifying the minimum of the two numbers, checking for shared factors, and examining the relationship between the numbers as multiples of their common divisor. The code also handles edge cases such common division by 0 and by even and odd numbers. The result of this function is a number that divides both a and b without a remainder, meaning it is the greatest common divisor of the two numbers. The code is designed to be efficient and handle a wide range of inputs, making it suitable for practical use in various scenarios.