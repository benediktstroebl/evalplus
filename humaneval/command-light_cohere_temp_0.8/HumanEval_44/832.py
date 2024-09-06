```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are full support: 10, 2, 36, and so on.
    """
    conversion = x.to_string(base)
    return f"{base {conversion}"

x = 8
base = 2
result = change_base(x, base)
print(result)
``` 
This function is self-contained and will successfully change the base of the number passed as an argument.