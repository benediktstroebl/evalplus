```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    # Define a function to convert a number into an array of digits
    def number_to_digits(number):
        return [int(x) for x in str(number)]

    # Define a helper function to extract the integer part
    def integer_part(digits):
        return max(digits, default=0)

    # Define a helper function to extract the decimal part
    def decimal_part(digits):
        return sum([1 for x in reversed(digits) if x != 0])

    # Define a helper function to get the decimal part as a fraction of 1
    def fraction(decimal_part):
        return decimal_part / 1

    # Define a helper function to check if a number is positive
    def is_positive(number):
        return number > 0

    # Define the main function that returns the decimal part of a number
    def truncate_number(number):
        # Check if the number is positive
        if is_positive(number):
            # Return the decimal part
            return fraction(decimal_part(number_to_digits(number)))
        # Otherwise return 0 (negative numbers are invalid for this problem)
        return 0
```
This script defines a function called `truncate_number` that takes a float number as input and returns the decimal part of the number. The function first checks if the number is positive, and if so, returns the decimal part as a fraction of 1. If the number is negative, the function returns 0, since negative numbers are not valid for this problem.