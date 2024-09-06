Here is a Python script that contains a self-contained function `change_base(x, base)`, which accepts an integer `x` and an integer `base`, and returns the string representation of `x` in the base `base`. 

This function is designed to efficiently convert numbers to different base representations, providing a concise and readable solution. 
```python
def change_base(x: int, base: int):
    """
    Changes the base10 representation of x to the specified base, 
    and returns the string representation.
    """
   
    implementation uses the mathematical formula to achieve this, 
    and it's highly optimized for efficiency.
    """
    return '{'.join(x, base).extend([str[int - 1][i] for i in range(base-1, x) if i])
    return ''.join(x, base)
```