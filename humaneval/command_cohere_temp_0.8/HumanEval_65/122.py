```python
def circular_shift(x, shift):
    num_digits = len(str(x))
    if shift > num_digits:
        shift = num_digits
    return int(str(x)[shift:] + str(x)[:shift])
```