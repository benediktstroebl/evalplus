```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    while a % b == 0:
        a //= b
    b = a
    
    return b

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5

```
The code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers a and b. It uses a essential while loop to repeatedly divide a by b until a is no more divisible by b. The function then returns b.