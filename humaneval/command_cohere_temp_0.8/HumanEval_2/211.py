```python
def truncate_number(number):
    return number - int(number)
```

The provided Python script defines a function `truncate_number` that takes a single argument, `number`, which is expected to be a positive floating point number. The purpose of this function is to extract and return the decimal part of the input number. This is achieved by utilizing the fact that floating-point numbers can be represented as a combination of an integer part (the largest integer less than or equal to the number) and a fractional part (the remaining value after removing the integer part).

The function uses the integer division (`//`) to calculate the largest integer less than or equal to the input number, and then subtracts this integer part from the original number. The result of this subtraction is the fractional part of the input number, which is then returned as the output of the function.

The function does not have any dependencies on external modules or libraries, making it self-contained and easy to use in any Python environment. Additionally, it is importantly noted that the function assumes that the input number is positive, and does not handle cases where the number is negative or contains special characters that could potentially trigger exceptions. 

To handle edge cases and avoid potential bugs or unexpected behavior, it is advisable to include explicit tests for edge cases and negative numbers in the input when using this function in a broader context.