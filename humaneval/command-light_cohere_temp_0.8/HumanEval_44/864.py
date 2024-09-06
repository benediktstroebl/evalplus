```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base.
    Return string representation after conversion
   
    base numbers are 10 based
    """
    if x < 0:
        raise ValueError("Input cannot be negative")
    elif base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    else:
        # Perform the conversion
        return format(x, f'{base}')
``` 
This code defines a function change_base that takes two parameters: x, which is the number to be converted, and base, which is the base to which the conversion will be performed. The function checks for valid input values and raises a ValueError with an appropriate error message if the input is not valid. The function then performs the base conversion using the format() function, which takes two arguments: the number to be formatted and the format specification.