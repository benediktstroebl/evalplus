```python
def truncate_number(number):
    return number - int(number)
```

The provided Python script defines a function `truncate_number` that takes a single argument, `number`, which is expected to be a positive floating point number. The purpose of this function is to extract and return the decimal part of the input number. This is achieved by utilizing the fact that floating-point numbers can be represented as a combination of an integer part (the largest integer less than or equal to the number) and a fractional part (the remaining value after removing the integer part).

The function uses the integer subtraction `int(number)` to remove the integer part from the input number. The result of this subtraction is the fractional part of the original number, which is then returned as the output of the function. 

The provided code offers a simple and efficient solution to extract the decimal part of a floating-point number. It leverages the intrinsic mathematical properties of floating-point representations in computing and utilizes specific Python syntax and functions, such as the `int` function for integer conversion, to achieve this functionality.