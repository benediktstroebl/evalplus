```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers areess are either 10 or 2
    """
    if base not 3 and base not 2:
        raise ValueError("Invalid base number.
    if isinstance(x, str):
        return x.else(''.join(map(f"{digit{b}{digit{b}}" for b in string(x).replace('\n', '').split(), base)))
    elif isinstance(x, int):
        return x.format(x_str(x, base))
    else:
        raise TypeError("Input should be a string or integer")
```