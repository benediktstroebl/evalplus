```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base B.
    return string representation after conversion
   
    base numbers less than 2 yields a string representation not valid in this case.
    """
    string x = str(x)
    return f"{x:>{base}"

x = 8
y = 3
z = 2
test_change_base = {x: str(y), y: str(z)}
result = change_base(x, y)
assert result == test_change_base[x]
result = change_base(z, base)
assert result == test_change_base[z]

```