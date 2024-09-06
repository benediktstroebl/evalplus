```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of the input number.
    base numbers 10.
    return string representation after conversion.
    """
    specific base number
   
    """
    if x < 0 or base < 2:
        raise ValueError("Invalid base or number")
    if base == 2:
        return '10' + str(x)
    else:
        return '{0}' + ''.join(str(x), base)
    """
    return x

x = int(input("Enter a number: "))
base = int(input("Enter the base: "))

result = change_base(x, base)
print(f"Result: {result}")
```