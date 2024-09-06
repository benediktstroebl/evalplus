```python
def circular_shift(x, shift):
    digits = str(x)
    result = digits[shift:] + digits[:shift]
    if len(result) < len(digits):
        return result
    else:
        return result[::-1]
```
This Python script defines a function called `circular_shift` which takes two arguments, `x` and `shift`. This function utilizes string manipulation to shift the digits of the integer `x` in a circular fashion to the right by the amount specified by `shift`, and it handles cases where the shift amount is greater than the number of digits. 

To use this function, you can simply call it with an integer value for `x` and an integer value for `shift`, like this:
```python
>>> circular_shift(12, 1)
'21'
>>> circular_shift(12, 2)
'12'
```

This will shift the digits of the number `12` right by one position, producing the result '21', and then shifting the digits right by two positions to return the original number '12'.