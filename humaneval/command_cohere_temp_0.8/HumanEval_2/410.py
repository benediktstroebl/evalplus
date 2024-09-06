```python
def truncate_number(number):
    return number - int(number)
```

The provided Python script defines a function `truncate_number` that takes a single argument, `number`, which is expected to be a positive floating-point number. The purpose of this function is to return the decimal part of the input number. This is achieved by subtracting the nearest integer (rounded down) from the input number. This integer part represents the largest integer less than or equal to the input number, and the difference obtained is the remaining fractional part, which is always less than or equal to 1. 

For example, if the input is `3.5`, the function computes `3 - 3 = 0.5`, which is then returned as the decimal part. 

The script assumes that the input number is valid, i.e., it adheres to the problem statement's requirement of being a positive floating-point number. Additionally, it assumes that the internal data type used to represent floating-point numbers in Python is capable of accurately representing the decimal part of the input number. 

This function does not check for negative numbers, decimal values, or infinity, as those cases go beyond the scope of the problem statement. Additionally, it does not handle any unusual characteristics specific to the floating-point arithmetic implementation on a particular platform or language version, such as rounding errors or loss of precision. 

Note that the function assumes the underlying data type used to represent floating-point numbers in Python supports the accurate representation and manipulation of floating-point values, and it implicitly relies on this assumption. 

It's crucial to note that this solution is based on the assumption that the input number is a positive floating-point number. If the input variable could be any real number, the solution may not work as expected.