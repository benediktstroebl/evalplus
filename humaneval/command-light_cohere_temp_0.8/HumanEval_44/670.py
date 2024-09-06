```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of a number to the specified base.
    Args:
        x: int, Input number
        base: int, Base to convert to
    Returns:
        string representation of the number
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    if x < 0:
        raise ValueError("Input number cannot be negative")
    s = str(x)
    if len(s) < 2:
        raise ValueError("Input number too small")
    return s[::-1].lstrip(s) if s[0] == '0' else s
```
The function change_base takes two arguments: x, which is the input number, and base, which is the base to which the input number will be converted. It returns a source number in the desired base, it first checks the validity of the base and input number, and raises appropriate exceptions if they are not valid. The function then converts the number to the desired base by using slicing and converting the last character to the reverse of the original string representation.