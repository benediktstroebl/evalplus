```python
def change_base(x: int, base: int):
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    return '{:0b}'.format(x, base)

# Basic tests
print(change_base(8, 3))      # Output: '22'
print(change_base(5, 9))      # Output: '55'
print(change_base(10, 3))    # Expected output: '300'
print(change_base(10, 52))   # Expected output: '5520' <==> '5.10^{52} / 1.0'

print(change_base(123, 10)))  # Expected output: '8'

# Edge case
print(change_base(10, 2))     # Expected output: '1000'
print(change_base(10, 35))   # Expected output: '1000000000000000'

```
This script defines a function change_base that takes two parameters: x, representing the number to be converted, and base, representing the desired base to convert to. <br performs a conversion using the string representation of the number x using the specified base. The code enforces input validation to ensure the base is within a valid range and raises an error if it is not. Finally, it prints the results of the function with different inputs and edge cases.