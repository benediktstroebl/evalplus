```python
def truncate_number(number):
    return number - int(number)
```

The provided Python script defines a function `truncate_number` that takes a single argument, `number`, which is expected to be a positive floating point number. The purpose of this function is to extract and return the decimal part of the input number. This is achieved by utilizing the fact that floating-point numbers can be expressed as a combination of an integer part (the largest integer less than or equal to the number) and a fractional part (the remaining value after removing the integer part).

The function uses the integer division (`//`) to calculate the largest integer that can be subtracted from the input number, leaving behind the fractional part. The `int()` function is then used to convert this difference to an integer, effectively removing the fractional part from the result. The resulting decimal value is then returned as the output.

This approach is both concise and efficient, utilizing built-in Python functionalities to achieve the desired result without requiring explicit looping or iterative processes. It appropriately addresses the problem statement by extracting the decimal part of the input number and providing a clear and understandable solution.