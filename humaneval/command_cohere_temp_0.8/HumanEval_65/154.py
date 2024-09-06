```python
def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:]+digits[:-shift] if len(digits) >= shift else digits[::-1]
```
This function shifts the digits of the integer `x` right by `shift` using the circular shift algorithm. If the shift is greater than the number of digits, it reverses the digits. The function takes an integer and an integer as inputs and returns a string.

Here is an example usage of the function:
```python
circular_shift(12, 1) # Outputs "21"
circular_shift(12, 2) # Outputs "12"
```

This algorithm can efficiently perform circular shifts of digits, providing a straightforward way to manipulate string-based numbers.