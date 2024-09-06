Here is a Python script that demonstrates a self-contained function to solve the markdown code block problem:
```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
        and integer part (largest integer smaller than given number) and decimals
        (leftover part always smaller than 1).

        Returns: decimal part of the number."""

    # Convert floating point number to a string
    number_str = str(number)

    # Remove non-decimal characters and convert to lowercase
    number_str = number_str.replace(str.maketrans('','.lowercase)

    # Split the number string into list of digits
    number_parts = list(number_str)

    # Sort the list of digits
    number_parts.sort()

    number_parts

    # Remove the leading 0 from the number string and get the last digit
    last_digit = number_parts.pop(0)

    # Calculate the integer part
    integer_part = 1 if last_digit == '' else int(last_digit)

    # Calculate the decimal part
    decimal_part = float(''.joinleaving(number_parts, 0))

    # Return the decimal part
    return decimal_part
```
This Python code defines a function `truncate_number` that takes a positive floating point number as input and returns the decimal part of the number.

The function first converts the input number to a string and removes non-decimal characters and converts it to lowercase. Then, it splits the string into a list of digits and sorts them. It removes the leading 0 from the list of digits and gets the last digit, which represents the integer part. Finally, it calculates the decimal part by removing the integer part from the sorted list of digits.