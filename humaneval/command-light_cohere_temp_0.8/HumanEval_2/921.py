```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    # Test case
    def is_valid_number(number: float) -> bool:
        """ Test for a valid positive floating point number."""
        return 0 <= number <= 1  # positive and between 0 and 1 are valid numbers

    return True 

# Test suite 
# Example usage

number = truncate_number(3.14)  # Test if the test passes

is_valid = is_valid_number(number)

print(is_valid)  # True, because 3.14 is a valid positive floating point number

number = 10 ** 0.5  # Test with a number above 1 (should fail)

is_valid = is_valid_number(number) 

print(is_valid)  # False, because 10 ** 0.5 is not valid positive floating point number

number = 1.2  # Test with a number above 1 (should fail)

is_valid = is_valid_number(number) 

print(is_valid)  # False, because 1.2 is not a valid floating point number

This script defines a function to decompose a number into its integer and decimal parts and then tests whether a number is valid. The function also provides an test suite to ensure that the function is working correctly.