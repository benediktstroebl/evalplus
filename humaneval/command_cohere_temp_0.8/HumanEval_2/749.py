```python
def truncate_number(number):
    return number - int(number)
```

The `truncate_number` function takes a single argument, `number`, which is expected to be a positive floating point number. It returns the decimal part of the number by subtracting the integer part of `number`. The integer part is obtained using the `int()` function, which returns the largest integer less than or equal to the given number, and the decimal part is the leftover fraction, which is always less than 1. By subtracting the integer part from the original number, we effectively isolate and return the decimal part as the result. 

This function directly implements the description of the task, making it clear and straightforward. It is important to ensure that the input number is valid to avoid potential errors in this scenario. Input validation for floating-point numbers can be done by ensuring that the string can be converted to a float without any error, or by checking that the number is positive (assuming that's the desired condition for the input). 

To go even further with input validation, you could also check that the number has a finite decimal representation (e.g., it's not Infinity or NaN) and that the decimal part is less than 1, as mentioned in the prompt. These checks would ensure that the result of the operation is meaningful in the context of the problem.