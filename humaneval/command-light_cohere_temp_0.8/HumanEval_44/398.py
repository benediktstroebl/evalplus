```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base B.
    """
    return a number as a string in the specified base.
    """
    print("input number: ", x)
    print("base: ", base)
    base = str(base)
    # convert to int to avoid issues with floating-point bases
    x = int(x)
    res = ''
    while x:
        # find first non-zero digit in x
        if x.isdigit(x):
            res = str(x % 10) + res
        else:
            break
        x //= 10
    return res
```