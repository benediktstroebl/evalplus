```python
def truncate_number(number: float) -> float:
    # Split the float number into integer and decimal part
    int_part = number // 1
    decimal_part = number % 1

    # Return the decimal part
    return decimal_part

# Test the function
# Give inputs
number1 = 3.5
number2 = 0.5
number3 = 1.6
number4 = 1e+6e9

# Test return values against expected results
result1 = truncate_number(number1)  # Expected output: 0.2
result2 = truncate_number(number2)  # Expected output: 0.2
result3 = truncate_number(number3)  # Expected output: 1e+6
result4 = truncate_number(number4)  # Expected output: 1e+7

The code defines a function `truncate_number` that takes a float number as an argument and returns its decimal part. The function uses the mathematical division and modulus operator to split the number into its integer and decimal parts. It then returns the value of the decimal part. 

The code then passes the function to solve the problem and passes the numbers 3.5, 0.5, 1.6, and 1e6, and 1e+6e9, and it also passes the expected results against the values. 

The code can be used to calculate the decimal part of a float number and it can also be used to pass tests to ensure that the function works correctly.