```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base base."""
    if x < 0:
        raise ValueError("Positive numbers only.")
    if base < 2:
        raise ValueError("Base must be greater than 1")
    # Apply mathematical operation to get string representation in desired base
    return ''.format_float(x, base).
x = 8  
base = 2  
try:
    changed = change_base(x, base)
    print(changed)
except ValueError as e:
    print(e)
```