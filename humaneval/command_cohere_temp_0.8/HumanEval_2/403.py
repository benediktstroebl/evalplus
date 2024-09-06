```python
def truncate_number(number):
    return number - int(number)
```
This Python script defines a function called `truncate_number` that takes in a single argument, `number`, which is a floating-point number. Inside the function, the `int` function is used to convert the input number to an integer, which effectively discards the decimal part of the number. The result is the difference between the original number and the integer part. This difference is returned as the output of the function.

The function is designed to handle floating-point numbers that have decimal parts, and it's particularly useful when you need to isolate and work with just the decimal part of a number while discarding the integer part.

This simple approach leverages Python's automatic floating-point arithmetic to do the right thing with decimal computations. Given that the test case `truncate_number(3.5)` returns 0.5, it confirms the correct functionality of the function.

This is a straightforward solution, but it might not be robust for very large or small numbers, or those that have a lot of decimal places. In such cases, this simplistic approach may lead to unexpected outcomes. Therefore, it's essential to understand the domain in which this function will operate before committing it to production. 

Furthermore, the function makes no assumptions about the validity of the input. If a user somehow passes in an invalid string or non-numeric value, the function, without any input validation, will proceed with the subtraction operation, potentially leading to errors or unexpected results. Hence, it's always advisable to ensure the input is of the expected type and within a valid range for the function to work as expected.