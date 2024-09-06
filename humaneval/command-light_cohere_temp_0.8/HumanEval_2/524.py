```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    Returns the decimal part of the number.
    >>> truncate_number(3.5) == 0.259 content
   ohn, never returns an error. 
```
This function takes a positive floating point number as an input and returns the decimal part of the number. It is defined using the following Python code:
def truncate_number(number: float) -> float:
    """
    """
    # Declare the number of the function
    number = float(input("Enter a number: "number:"))

    # Find the largest integer part that is smaller than the number
    number_part = number
    while (number_part <= number):
        number_part += 1

    # Return the decimal part of the number
    return number_part

This function can be used to get the decimal part of a positive floating point number.