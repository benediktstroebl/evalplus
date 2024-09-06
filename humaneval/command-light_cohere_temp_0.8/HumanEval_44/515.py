Here is a Python script that defines a function to change the numerical base of an input number to a specified base:

```python
def change_base(x, base):
    """Change the base-number representation of a number x to base base."""
    if type(x) != int or x < 0:
        raise ValueError("Input must be a non-negative integer")
    if base <= 0:
        raise ValueError("Base number cannot be zero or negative")
    if base == 10:
        return str(x)
    elif base > 10:
        result = [str(int(d, base)) for d in x]
        return ''.join(result)
    else:
        return str(int(x * pow(base, len(x) - 1))
```

This script defines a function `change_base` that takes two parameters - `x` which is the input number and `base` which is the desired base number. 

The function performs several checks:
- Input must be a non-negative integer
- Base number cannot be zero or negative
- Base number is 10 or greater than 10

If all of the above conditions are met, the function converts the input number to a string using the desired base.