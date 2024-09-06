```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    return_str = str(number)
    return float(int(return_str[0:1]) + float(return_str[2:]))
```

This function takes a number as input and returns the decimal part of the number.  It achieves this by: 
 - Converting the given number to a string using the str() function.
- Extracting the integer part and the decimal part of the string using string slicing and the int() function.
- Adding the integer part and the decimal part to get the desired decimal part.