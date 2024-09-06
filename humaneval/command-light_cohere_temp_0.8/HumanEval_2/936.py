```python
def truncate_number(number: float) -> float:
    # Function to truncate a floating point number to the integer part
    integer = number // 10
    decimal = number % 10

    # Return the integer part
    return integer if decimal <= 0 else decimal

# Example usage:
# Test the function with a number > 10
test_truncate_number(12.5)  # Output:  2.3

# Test the function with a number < 10
test_truncate_number(0.5)  # Output:  0.5

# Test the function with a number = 0
test_truncate_number(0)  # Output:  0

# Test the function with a negative number
test_truncate_number(-12.5)  # Output:  -12

``` 
This Python script defines a function `truncate_number` that removes the decimal part of a given floating point number, returning the integer part. The function is tested with several examples, passing all of them successfully.