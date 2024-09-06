```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10
   
    whole numbers
    """
    if x < 0:
        return "Error: Input number should be positive"
    if base < 2 or base > 36:
        return "Error: Base number should be between 2 and 36"
    if x < base:
        return f"{x} is less than base number"
    return format(x, f"{base} base", "g")

print(change_base(8, 3)) # 22
print(change_base(7, 2)) # 111
print(change_base(-3, 10)) # Error: Input number should be positive
print(change_base(10, 10)) # Error: Base number should be between 2 and 36
```