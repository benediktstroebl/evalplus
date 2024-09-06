```python
def truncate_number(n: float) -> float:
    if n < 0:
        return "Error: Input must be a positive number."
    if not isinstance(n, float):
        return "Error: Input must be a float"
    return round(n)
``` 
This Python function, named `truncate_number`, is designed to remove the decimal part of a positive floating-point input `n`. It performs this by utilizing the `round()` function, which returns the nearest whole number to the input.

Here's a breakdown of the function's operation:
1. Ensure the input `n` is a positive number: If `n` is less than 0, it will return an error message indicating that the input must be a positive number.
2. Check the type of input: If `n` is not a float, it will return another error message.
3. Calculate the decimal part: It does this by calling `round()` with `n`, which removes the decimal part of the number.

Finally, the function returns the rounded value of `n`, which has the decimal part removed. 

This function is self-contained, and it can be used to truncate a positive floating-point number to its decimal part, without the need for additional external functions or variables.