```python
def change_base(x, base):
    return str(x).convert(base)
```
This function uses the `.convert()` method from Python3 to convert the decimal number `x` into the given `base`. This method works for bases less than `10` as it accepts the base as a numeric value and returns the converted number as a string. Thus, no additional checks are needed for bases less than `10`.