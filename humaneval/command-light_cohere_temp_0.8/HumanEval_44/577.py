```python
def change_base(x: int, base: int) -> str:
    """Change the base of a number x to a specified base."""
    if base == 10:
        return str(x)
    return str(x, base)

# tests
print(change_base(8, 3))  # expected output '22'
print(change_base(10, 2))  # expected output '1000'
print(change_base(10, 5))  # expected output '5'
print(change_base(123, 2))  # expected output '0'
print(change_base(123, 1))  # expected output '1'
print(change_base(123, 4))  # expected output '0422'''
```
This code defines a function `change_base` that takes two parameters: `x` (the number to be converted) and `base` (the desired base). The function then performs the necessary conversion and returns the string representation of the number in the desired base. 

Note that the above code is self-contained, and it does not require any additional variables or external functions.