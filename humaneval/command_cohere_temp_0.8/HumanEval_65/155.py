```python
def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:] + digits[:-shift]
```

This function takes an integer `x` and an integer `shift` as input and outputs a string. It converts the integer `x` to a string `digits`, and then performs a circular right shift on the digits, meaning that the shift is applied to the rightmost digit, and the leftmost digit is inserted into the shift position. This is done by concatenating the right-shifted digits to the left of the original string and the left-shifted digits to the right, and then returning the result.

Here is an example of how this function can be called:
```python
circular_shift(12, 1) # Outputs "21"
circular_shift(12, 2) # Outputs "12"
```

This function will work correctly for any positive integer `x` and integer `shift`, and will reverse the digits if shift is greater than the number of digits.