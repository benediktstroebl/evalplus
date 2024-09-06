```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return "Error: One or both arguments is not a number"
    if a == 0:
        return "Error: Division by zero"
    # Note: b can be negative, so we handle it
    while b != 0:
        a, b = b, a % b
    return a
``` 
This function is designed to find the greatest common divisor of two integers a and b, handling edge cases such as division by zero and invalid inputs.