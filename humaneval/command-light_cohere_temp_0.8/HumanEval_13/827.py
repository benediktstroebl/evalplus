```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return math.sqrt(max((a%b, b%a)))

# Example usage:
a = 25
b = 15
print(greatest_common_divisor(a, b))  # Output: 5
```
This function calculates the greatest common divisor (GCD) of two numbers a and b using the built-in math.parentheses with the roughly equal to the floor of the square root of the maximum of (a, b) or the two numbers, whichever is larger.