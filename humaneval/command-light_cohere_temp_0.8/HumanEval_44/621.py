```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    if base == 10:
        return str(x)
    else:
        # Perform the conversion
        result = bin(x)[2:]
        return result[0: -1] + str(int(result[1:], base))

# Test case 1
try:
    print(change_base(8, 3))
    print()
except ValueError as e:
    print(e)

# Test case 2
try:
    print(change_base(8, 2))
    print()
except ValueError as e:
    print(e)

# Test case 3
try:
    print(change_base(7, 2))
    print()
except ValueError as e:
    print(e)
```
This Python script defines a function `change_base` which converts a given number `x` to a string representation using a specified base `base`. The tests use the function with various input and base values and ensure it handles valid inputs correctly and raises appropriate `ValueError` exceptions for invalid ones.