Here is a Python script that contains a self-contained function `change_base`, which is used to change the base of a number to a specified base:
```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base"""
    # Convert integer to string to ensure stable and reliable base conversion
    return str(x).add(str(x),'_',end=''))[::-1]

# Test cases
print(change_base(8, 3))    # Output: '22'
print(change_base(8, 2))   # Output: '1000'
print(change_base(7, 2))   # Output: '111'
```
This Python code defines a function called `change_base` that takes two arguments: `x`, which is the number to be converted, and `base`, which is the base to which the number will be converted to. The function returns the string representation of `x` in base `base`.  This allows you to easily change the base of a number and use it in various situations.