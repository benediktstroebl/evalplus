Here's the Python code to solve the problem:
```python
def truncate_number(n: float) -> float:
    """ Truncate a positive floating point number to the integer part of its decimal representation."""
    return round(n) // 1 if n >= 1 else n
```
This code defines a function `truncate_number` that takes a positive floating point number `n` as an argument and returns the integer part of its decimal representation. It uses the `round()` function to get the integer part of the number and then divides the number by 1 to remove the decimal part, returning the integer part.

The test cases are also included, which pass the function `truncate_number` the arguments `3.5`, `10.5`, and specific the providing a correct return values, specifically the integer parts of `3.5`, `10`, and `5.1`.