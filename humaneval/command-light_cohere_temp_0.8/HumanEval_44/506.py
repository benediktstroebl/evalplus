```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    convert to string
   
    base numbers use the base10 digits and will start from 0 or 1 depending on the value of the number.
    """
    number to be represented in base 10 (decimal)
    """
    # Ensure the number is positive
    if x < 0:
        x = abs(x)

    # Apply formula for conversion
    base_digits = [str(i) for i, j in enumerate(str(x), base)]
    # Remove extra base digits that are 0 or less than j
    while any(base_digits) and base_digits[-1] < base:
        base_digits.pop()

    format(base)
    # Return the number as a string
    return format(x, 'b{}'[base_digits])

x = int(input("Enter a number: "))
base = int(input("Enter the base to convert to: "))

result = change_base(x, base)
print("Result:", result)
```