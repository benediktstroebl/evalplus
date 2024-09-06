```python
def circular_shift(x, shift):
    digits = str(x)
    result = digits[shift:] + digits[:shift]
    if len(result) > len(digits):
        result = result[::-1]
    return result
```

This approach first splits the integer into a list of digits, then shifts the digits along the list, and lastly concatenates the shifted digits back into a string. Shifting further than the length of the digits will return the digits reversed.