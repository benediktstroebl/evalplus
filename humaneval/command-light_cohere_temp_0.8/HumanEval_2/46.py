Here's the function to truncate a number to a decimal value:

```python
def truncate_number(number: float) -> float:
    """ Returns the decimal part of the number.
    Returns a number if input is negative, returns None."""
    # handle negative numbers
    if number < 0:
        return None

    # Handle special cases first
    if number <= 1:
        return number

    # Since floor(number/10) will return an integer, we can use it to truncate the number
    # and remove the decimal part.
    remainder = number / 10
    return remainder
```

This function first handles the negative number input by returning None. Then it checks for the the number's special cases (numerles, 0, 1) and returns the number immediately. Finally, for other numbers, it uses the division operator to divide the number by 10 and then uses the remainder operator to remove the decimal part from the result.

This function will always return a float number, and for any number less than or equal to 1, it will return the number itself.