### Truncating Decimal Part of a Number

Here is a Python function that fulfills the given requirements:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # We use the int() function to truncate the number, which returns the largest integer less than or equal to the given number
    integer_part = int(number)
    
    # To get the decimal part, we subtract the integer part from the original number
    decimal_part = number - integer_part
    
    return decimal_part
```
You can use this function like this:
```python
print(truncate_number(3.5))  # Outputs: 0.5
print(truncate_number(10.7))  # Outputs: 0.7
```
This function works by first truncating the number to its integer part using the `int()` function. Then, it calculates the decimal part by subtracting the integer part from the original number. The result is the decimal part of the input number.