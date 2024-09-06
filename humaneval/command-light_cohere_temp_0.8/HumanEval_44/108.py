```python
def change_base(x: int, base: int):
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    return '{:0b}'.format(x, base)

x = 8
y = 3
z = 2
try:
    print(change_base(x, y))
    print(change_base(x, z))
    print(change_base(z, y))
    print(change_base(z, z))
except ValueError as e:
    print(e)
```