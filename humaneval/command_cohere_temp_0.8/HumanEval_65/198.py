```python
def circular_shift(x, shift):
    s = str(x)
    digits = len(s)
    if shift > digits:
        shift = shift % digits
    return s[shift:] + s[:shift]
```

This code provides a solution to the problem by shifting the digits of the string representation of **x** to the right by **shift**. In addition, if `shift` is greater than the number of digits, it performs a modulo operation to iterate the string accordingly. 

Here is an example usage of the function where it shifts the number 12 by 1 and 2 respectively:
```python
circular_shift(12, 1)  # "21"
circular_shift(12, 2)  # "12"
```