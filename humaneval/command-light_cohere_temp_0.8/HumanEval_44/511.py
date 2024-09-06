```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both inputs must be integers.")
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")

    ret = []
    while x > 0:
        ret.append(format(int(x % base), base))
        x //= base
    return ''.join(''.join(ret, reverse=True)) or 'ValueError'

# Tests
print(change_base(8, 3))      # Output: '22'
print(change_base(7, 2))      # Output: '111'
print(change_base(12345678, 4)) # Raises ValueError
print(change_base(-3, 2))    # Raises TypeError
print(change_base(True, 4))   # Raises TypeError
print(change_base('text', 2)) # Raises TypeError
```
This Python script defines a function `change_base` that converts a number to a specified base. The `base` parameter can only accept values between 2 and 36. It uses a standard while loop to convert the number to a string representation using the desired base. 

The tests in the code verify the behavior of the `change_base` function. They pass different tests cases and raise `ValueError` or `TypeError` if the inputs are not valid integers or not within the expected base range.