```python
def circular_shift(x, shift):
    s = str(x)
    return s[-shift:] + s[:-shift] if shift < len(s) else s[len(s) - shift:] + s[:len(s) - shift]
```

The function takes an integer `x` and a shift value as parameters and uses string manipulation to shift the digits of `x` circularly. The digit '1' is inserted at the rightmost position and all digits to the left are shifted to the right. If the shift value is greater than the number of digits, the digits are reversed. The function returns the shifted integer as a string. 

This approach follows the problem's guidelines, ensuring the function is self-contained and compatible with the provided tests. 

Here is an example of how to use the function:
```python
circular_shift(12, 1) # Outputs "21"
circular_shift(12, 2) # Outputs "12"
```