```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    number = float(number)
    original_digits = len(str(number))

    decimal_part = 0
    while original_digits > 0:
        fractional_digit = number % 10
        decimal_part += fractional_digit
        number = number // 10
        original_digits -= 1

    return decimal_part

# Example usage
result = truncate_number(3.5) # Output: 0.3

result = truncate_number(0.0) # Output: 0.0

result = truncate_number(-3.0) # Error: Trace error

This code defines a function called `truncate_number` that takes a floating point number as an argument and returns the decimal part of the number. It uses a loop to repeatedly divide the number by 10 until it is less than 1, and adds the remainder to a running total of the fractional digits. The code then returns the decimal part of the original number.