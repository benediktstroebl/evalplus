```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
tests = [ (3.5, 0.5),  # Basic test case
         (2.5, 0.5),
         (1.0, 0.0),
         (1.5, 0.0),
         (11.45, 0.45),
         (1.79769e+308, 1.79769e+308) # Maximum positive value of float
        ]

for n, ex in tests:
    assert truncate_number(n) == ex
``` 
The function `truncate_number()` takes a single parameter, `number`, which is the number to be truncated. It returns the decimal part of the number by subtracting the integer part (obtained by rounding the number to the nearest integer) from the original number. This is done using the expression `number - round(number)`. The `round()` function rounds the number to the nearest integer, and the resulting difference gives the decimal part.

The test suite consists of `pytest` style tests, with each test consisting of a tuple containing the input number and the expected output. The `assert` statement checks that the output of the `truncate_number` function corresponds to the expected output for each test case.  It is important to note that this approach assumes the given number is in the standard single-precision or double-precision floating-point representation, as rounding to the nearest integer works differently for other floating-point formats. 

To run the tests, you can copy and paste this code into a Python interpreter or a Python script and execute it. 

This approach is not feasible in markdown and is better suited for a full programming language environment like Python. Test cases are also included to validate the correctness of the function against different inputs.