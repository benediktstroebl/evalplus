```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base
    """
    if not isinstance(x, (int, float)) or x < 0:
        raise TypeError("Input must be a number")
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    if base == 2:
        return str(x * int(base ** x))
    return str(int(base ** x))

# Unit tests
print(change_base(-3, 10))
print(change_base(0, 45))
print(change_base(7, 31))
print(change_base(123, 5))
print(change_base("123", 2))
print(change_base("0.3", 10))
```