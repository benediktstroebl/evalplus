```python
def truncate_number(n: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    return n if n >= 1 else 0.25  #n 

This Python code defines a function `truncate_number` that takes a floating-point number as input and returns the decimal part of that number. The function uses a conditional check to determine whether the input number is greater than 1 or not. If it is, the function returns 0.5. If the input is number, it returns the number itself, effectively discarding the decimal part.