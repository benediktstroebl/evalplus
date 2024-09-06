```python
def truncate_number(number):
    """ Returns the decimal part of the number
    Args:
        number (float): positive floating point number
    Returns:
        float: decimal part of the number
    """
    return number - int(number)
```

To better understand the logic behind the function, here is an explanation of how it works:
The function `truncate_number` takes a single argument, `number`, which is a positive floating point number. It returns the decimal part of the number as a float value. 

The decimal part of the number is the value after the decimal point. The function calculates this by subtracting the largest integer that is less than or equal to `number` from `number`. This is achieved by converting `number` to an integer using `int(number)`. The difference between the original number and the newly created integer is the desired decimal part of the number which is then returned.

For example, let's apply this function to the given test case from the prompt:
```python
>>> truncate_number(3.5)
0.5
```
This result demonstrates that the function correctly returns the decimal part of the number, which in this case is 0.5.