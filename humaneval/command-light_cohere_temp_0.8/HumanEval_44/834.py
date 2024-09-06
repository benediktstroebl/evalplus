```python
def change_base(x: int, base: int):
    """Change the numerical base of input number x to base B."""
    if base < 2 or base > 36:
        raise ValueError("Invalid base number. This base must be between 2 and 36.")
    return str(x)
x = 8
y = "3000"
z = change_base(x, y)
print(z)
```