```python
def truncate_number(number):
    """ Returns the decimal part of a positive floating point number. """
    return number - int(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.0) == 0.0
assert truncate_number(0.501) == 0.001
``` 

This script includes a function, `truncate_number`, that returns the decimal part of the input positive floating point number. It does so by taking the difference between the input `number` and its closest integer value using integer conversion, accomplished with the `int()` function. 

Three test cases are provided to demonstrate the function's behavior on different inputs and to ensure that the output is correct. 

To run the test cases, you can print the assertions one at a time or use a testing framework like `pytest` to automate the process and to easily add more test cases in the future. 
If you're interested in using `pytest`, I can provide instructions on how to set it up and structure your test cases. Don't hesitate to ask if you have any further questions!