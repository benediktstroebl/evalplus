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

To better understand the logic of the function let's analyze the steps of the provided solution:
1. `def truncate_number(number):`: The function takes a single argument named `number` which is of type `float`.
2. `return number - int(number)`: The core logic of the function is encapsulated in this line. Here's what happens in this step:
    - `int(number)`: The `int()` function converts the floating-point number to the nearest integer. The conversion rounds the number to the nearest integer according to the current system settings. This value is typically what you get when you type an integer in your terminal.
    - `number - int(number)`: The subtraction between the original number and the nearest integer. This operation results in either a subtraction if the number is greater than the nearest integer, or an addition if the number is less than the nearest integer. The result is that the integer part of the number is removed, and only the decimal part is kept. 

This result is always less than 1, and corresponds to the residual of the original number (i.e. the decimal part of it). 

For example, in `truncate_number(3.5)`, `3` is the largest integer smaller than `3.5`, so the subtraction results in `0.5`. 

The function returns this residual as the output, achieving the desired result. 

The function is self-contained, and achieves the goal without using any global variables or external imports. 

It can be tested against any valid floating-point number and it will consistently return the decimal part of it.