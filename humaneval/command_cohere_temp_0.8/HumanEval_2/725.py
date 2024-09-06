```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a positive floating point number as input and returns the decimal part of the number. It does so by taking the difference between the given number and the nearest integer (largest integer smaller than the given number), which is achieved by subtracting the integer conversion of the number from the number itself. This effectively isolates the residual decimal portion, which is then returned as the result. 

This approach leverages the fact that floating-point numbers can be decomposed into an integer part and a fractional part, where the fractional part always has a value less than 1. Therefore, the difference between the original number and the closest integer represents the fractional part of the number accurately. 

To test this script, you can call the `truncate_number` function with a floating-point input, such as `3.5`. The result should be `0.5`, which represents the decimal part of the original number. 

This approach is concise and straightforward, providing a minimal solution to the problem as asked.