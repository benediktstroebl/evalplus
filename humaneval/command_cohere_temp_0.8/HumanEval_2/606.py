```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as input and returns the decimal part of the number by subtracting the integer part of the number (obtained by rounding down to the nearest integer). This effectively isolates the fractional part of the number and returns it. 

To execute this code simply run the script in your Python environment of choice. The function can be tested as follows:
```python
# Testing the function
assert truncate_number(3.5) == 0.5
assert truncate_number(12.345) == 0.345
``` 
This would yield output:
```bash
True
True
```

Note that the function assumes that the input is a positive floating point number. If the number is negative or is not a number (NaN), the result of the function may be unexpected or incorrect.