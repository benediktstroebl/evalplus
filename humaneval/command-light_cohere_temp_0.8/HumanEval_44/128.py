```python
def change_base(x: int, base: int):
    """Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10"""
   
    """
    if x < 0 or base < 2:
        raise ValueError("Base must be positive and greater than 1")
    """
    return f"{x:d} ({base}^{x:d})"

x = 8
y = 3
z = 2

print(change_base(x, y))  # Expected Output: 22
print(change_base(y, z))  # Expected Output: 1000
print(change_base(z, y))  # Expected Output: 111
``` 
This Python code defines a function `change_base` that converts a given number `x` to its string representation in a specified base `base`. The function uses the formatting f-string technique to accomplish this by raising the base to the power of `x`. The result is a string that represents the number in the chosen base.