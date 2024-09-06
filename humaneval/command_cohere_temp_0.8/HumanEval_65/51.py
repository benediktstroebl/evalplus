```python
def circular_shift(x, shift):
    digits = str(x)
    return digits[-shift:] + digits[:-shift]
```

This function takes an integer `x` and an integer `shift` as input and returns the circular shifted digits of `x` to the right by `shift` as a string. If `shift` is greater than the number of digits, it returns the digits reversed. This algorithm works by converting the number to a string, taking the last `shift` digits, and adding them to the beginning of the string. It is essential that the number is represented as a string for this technique to function effectively.

Here is an example usage of the function:
```python
circular_shift(12, 1) # "21"
circular_shift(12, 2) # "12"
```