```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    integer = int(n)
    decimal = n - integer
    return decimal
``` 
This Python function, named `truncate_number`, is designed to extract the decimal portion of a given positive floating-point number `n`. The function employs the built-in function `int` to represent the integer part of `n`, and then calculates the decimal part by subtracting the result of `int` from `n`. This function effectively isolates the decimal portion, which is the desired output.