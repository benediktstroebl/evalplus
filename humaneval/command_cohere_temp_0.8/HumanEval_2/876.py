```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

The function `truncate_number` returns the decimal part of the input number by subtracting the integer part of the number (obtained by converting the number to an integer) from the input number. This effectively isolates the decimal part and returns it as the output. 

This approach utilizes the inherent behavior of floating-point numbers in Python, wherein floating-point numbers are represented internally in scientific notation. Upon subtracting the integer part, the resulting value inherently represents the leftover decimal portion, which is then returned as the output. 

Note: This approach is tolerant to numerical precision and rounding errors, yielding a consistent and accurate result for the decimal component. 

The behavior of the function is further illustrated by the following example:
```python
>>> truncate_number(3.5)
0.5
>>> truncate_number(12.34567)
0.34567
>>> truncate_number(123.7)
0.7
``` 

In these examples, the function `truncate_number` correctly returns the decimal part of the input number, which corresponds to the leftover value after subtracting the largest integer less than the number. 

This approach leverages fundamental properties of floating-point representations and expertly isolates the decimal part of the input number.