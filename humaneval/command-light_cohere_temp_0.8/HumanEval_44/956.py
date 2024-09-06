```python
def change_base(x: int, base: int):
    """
    Change the base of input number x to base base.
    return string representation after conversion.
    base numbers are use 10
   
    """
    # check if the number is negative
    if x < 0:
        return 'negativized ' + change_base(-x, base)
        
    # check if the number is a fraction
    if x >= 1 and base == 2:
        return x*('0' + ('1' * ('0' + x)))
    # base is an odd number
    elif base > 2 and x % base == 0:
        return x // base
    # handle other cases
    else:
        return x if base > 0 else x * base
    return x
```