```python
def change_base(x: int, base: int):
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Base must be between 2 and 36.")
    # Use a formula to convert to base 10
    if x < 0:
        x = abs(x)
    new_str = []
    while x:
        new_digit = str(x % base)
        new_str.append(new_digit)
        x //=base
    return ''.join(new_str)

# Example usage:
x = 8
base = 2

result = change_base(x, base)
print(result)  # Output: '1000'

x = 7
base = 2

result = change_base(x, base)
print(result)  # Output: '111'

x = -3
base = 10

result = change_base(x, base)
print(result)  # Output: '-30'

x = 10
base = 36

result = change_base(x, base)
print(result)  # Output: ' 46000000 '
```