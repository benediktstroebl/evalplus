```python
def circular_shift(x, shift):
    s = str(x)
    digit_count = len(s)
    if shift > digit_count:
        return s[::-1]
    return s[-shift:] + s[:-shift]
```
This Python script defines a function `circular_shift` taking in two parameters, `x` and `shift`. This function performs a circular right shift of the decimal digits of `x` by `shift`, then returns the result as a string. If `shift` is greater than the number of digits in `x`, it reverses the digits instead. This aligns with the problem statement and test examples provided, where under such a shift, the leading digit(s) wrap around to become the trailing digit(s). 

Here is an example of how to use the function:
```python
circular_shift(12, 1) # "21"
circular_shift(12, 2) # "12"
```
This technique in digital signal processing is known as a circular shift, as opposed to a linear shift, which treats the digits as a linear sequence.