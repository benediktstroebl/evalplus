```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion
   
    base numbers under 10.
    """

    number to convert: x
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.
    return f"{x base}")[x // base] + str(x % base)

x = int(input("Enter a number: "))

base = int(input("Enter a base: "))

try:
    result = change_base(x, base)
    print(result)
except ValueError as ve:
    print(f"Error: {ve}")
```