```python
def truncate_number(number):
    return number - int(number)
```

The provided Python script defines a function `truncate_number` that takes a single argument, `number`, which is expected to be a positive floating point number. The purpose of this function is to return the decimal part of the input number. This is achieved by subtracting the largest integer that is less than or equal to the input number from the input number itself. This integer component captures the largest integer value that can be represented by the given number, and the remainder becomes the decimal part, which is returned by the function. 

For example, if the function is called with the input `7.5`, the function will return `0.5`, as the largest integer less than or equal to `7.5` is `7`, and subtracting `7` from `7.5` yields `0.5`. 

This approach utilizes the fact that floating point numbers can be represented as a sum of an integer and a fraction, where the integer represents the whole number part and the fraction represents the decimal part. 

Note: This function assumes that the input number is a positive floating point number. If the input can be negative or is not a number, more robust input validation and error handling would be necessary for practical applications.