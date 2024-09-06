```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

The function `truncate_number` accepts a single parameter, `number`, which is a positive floating point number. It returns the decimal part of the number by subtracting the integer part of the number from the input `number`. The integer part of the number is obtained using the `int()` function which returns the largest integer less than or equal to the given parameter. The remaining value is the residual decimal part of the original number, which is always less than or equal to 1. 

Here is an example of use:
```python
print(truncate_number(3.5))  # Should print: 0.5
``` 

This will output `0.5` as the residual decimal part of the original number. 

This script adequately solves the problem using an intuitive algorithm and adheres to Python's best practices with regards to variable naming and commenting.