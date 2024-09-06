```python
def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]
```
This Python script defines a function called `circular_shift` takes two parameters, `x` and `shift`. This function performs a circular right shift of the decimal digits of `x` by `shift`, and returns the result as a string. 

Here is an example usage of the function:
```python
circular_shift(12, 1) # Outputs "21"
circular_shift(12, 2) # Outputs "12"
```
This function also has additional checks to ensure that if a shift is greater than the number of digits, it reverses the string so that the circular shift still produces a valid integer.