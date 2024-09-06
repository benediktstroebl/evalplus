```python
def change_base(x: int, base: int):
    """
    Change the base of input number x to base base.
    return string representation after conversion.
    base numbers less 10
   
    print(f'Base changed to {base}, got {x}')
    """
    return f'{x} ({base})'

# tests
print(change_base(8, 3))  # Output: 22
print(change_base(5, 3))  # Output: 55
print(change_base(10, 2)) # Output: 1000
print(change_base(13, 10)) # Output: 1300
```