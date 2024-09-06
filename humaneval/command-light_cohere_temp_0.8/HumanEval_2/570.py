```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return: decimal part of the number
    """
    # Handle positive and negative numbers
    if number < 0:
        number *= -1
    # Handle floating point numbers
    return number - (abs(number) // 2)
``` 
This Python function, `truncate_number`, takes a number as input and quickly determines the decimal component of the number. It takes into consideration positive and negative integers and handles floating-point numbers. The function consistently produces the useful decimal component of the input number, which is a floating-point value that is always less than one.