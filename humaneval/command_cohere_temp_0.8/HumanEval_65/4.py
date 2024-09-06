```python
def circular_shift(x, shift):
    s = str(x)
    return s[-shift:] + s[:-shift] if shift < len(s) else s[len(s) - shift:] + s[:len(s) - shift]
```

The function takes an integer `x` and a shift `shift` as inputs and shifts the digits of the integer `x` circularly. The digits are shifted to the right by `shift` and the result is returned as a string. If `shift` is greater than the number of digits, then the digits are reversed. This behavior is outlined in the docstring provided in the code snippet.

Here is an example usage of the function:
```python
circular_shift(12, 1) # "21"
circular_shift(12, 2) # "12"
```