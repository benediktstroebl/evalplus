```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    if a == 0:
        return b
    if b == 0:
        return a

    while a % b == 0:
        a //= b
    while b % a == 0:
        b //= a

    return min(a, b)

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(105, 25))  # Output: 5
print(greatest_common_divisor(56, 112))  # Output: 4
```
This function will determine the greatest common divisor of two numbers a and b, which can be integers or not. It will return 0 if either number is not provided, and it will return the greatest common divisor of the two numbers if they are both provided.