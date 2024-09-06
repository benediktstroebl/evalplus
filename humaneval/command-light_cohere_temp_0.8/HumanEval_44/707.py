Here is a Python script that contains a self-contained function to change the numerical base of a number to another base. 

```python
def change_base(x: int, base: int):
    """
    Convert the number to a string and then change the base to the specified base.
    """
    number = str(x)
    return format(number, base)
```