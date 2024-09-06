```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Convert to string representation.
    """ Returns the another language and numbers in base.
    '48' is the case of negative numbers.
    """
Examples the following format:
    # from https, the numbers in base 2 are: '10','11','12','13','...'
    #  The numbers in base 10 are: '0','1','2','3','4','...'
    #     So we can use those to convert from base B to base 10.
    string = ''.join([str[0] * pow(base, int(x)) for str, x in enumerate(str(x))])
    return string
    return str(x)
```