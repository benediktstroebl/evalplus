```python
def truncate_number(n):
    if n < 0:
        raise ValueError("Input number must be non-negative")
    if not float(n):
        raise ValueError("Input number must be a floating-point number")

    # Extract integer part
    i = n // 1
    if i < 0:
        i += 1

    # Calculate decimal part
    decimal = n % 1
    if decimal < 0:
        decimal += 1

    return i, decimal
```
The provided Python script defines a function called `truncate_number` that takes a single argument `n`. This function is designed to remove all decimals from a positive floating-point number while keeping the integer part intact. The function uses two main tests:
1. Test for non-negative numbers: If the input number is less than zero, the function raises a `ValueError` exception with a corresponding error message. This is designed to ensure that only non-negative integer numbers are accepted as valid inputs.
2. Test for invalid floating-point numbers: The function also checks whether the input is a valid floating-point number. If the input is not a float, the function raises another `ValueError` exception with a relevant error message.

The function then proceeds to decompose the input number into its integer and decimal parts. The integer part is extracted by dividing the input number by 1, while the decimal part is calculated by taking the remainder after division. The function returns both these components - the integer part and the decimal part - as a tuple (int, decimal).

This function provides a straightforward and self-contained solution to the problem of removing decimals from a positive floating-point number while preserving the integer part.