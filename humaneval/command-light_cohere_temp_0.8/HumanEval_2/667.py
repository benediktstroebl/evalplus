Here's the Python code with a self-contained function that truncates a positive floating-point number to a decimal number:

```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part
```

This code defines a Python function `truncate_number` that takes a positive floating-point number as input and returns the decimal part of that number.

The function first computes the integer part of the number by calling the built-in function `int` on the number, then the decimal part is obtained by subtracting the integer part from the original number. The function then returns the `decimal_part`.

This code is a good example of a self-contained function, which has all the code required to be used within it, and it can be easily reused in other parts of the program.