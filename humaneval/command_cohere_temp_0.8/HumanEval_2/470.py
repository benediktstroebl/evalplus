```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
tests = [ (3.5, 0.5),
         (2.5, 0.5),
         (1.0, 0.),
         (1.5, 0.5),
         (11.05, 0.05),
         (100.566, 0.566)
      ]

for number, expected in tests:
    assert truncate_number(number) == expected
```
The function `truncate_number()` takes a float number as a parameter and returns the decimal part of the number. It does so by subtracting the integer part of the number (obtained by rounding the original number to the nearest integer) from the original number. The resulting difference should consist of the decimals that were originally part of the number. 

The test suite aims to validate this function with a variety of examples, ranging from numbers with zero decimal places to numbers with more than one decimal place. Each test consists of a pair with an input number and the expected output (the decimal part of the number). 

By using the `assert` statement, the script will produce an error message if the output of the `truncate_number()` function does not match the expected result from a particular test. This allows the script to act as a validation tool to ensure the function works as expected, providing a correct and understandable way of testing the code's functionality.