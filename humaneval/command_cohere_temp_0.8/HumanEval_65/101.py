```python
def circular_shift(x, shift):
    s = str(x)
    return s[-shift:] + s[:-shift] if shift < len(s) else s[len(s) - shift:] + s[:len(s) - shift]
```

The above function shifts the digits of the integer `x` right by `shift` taking into account the circular shift functionality if `shift` is greater than the number of digits.