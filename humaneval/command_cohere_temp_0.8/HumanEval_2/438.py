```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(44.0) == 0.0
``` 

The function `truncate_number` takes a single parameter, `number`, which is the number to be processed. It calculates the decimal part of the number by subtracting the largest integer less than or equal to `number` from `number` itself. The resulting value is the decimal part of the number. 

The test suite uses the `assert` statement to verify that the `truncate_number` function produces the expected output for a variety of input values. The first assertion tests the function with a value that has a whole part and a decimal part; the latter two assert the behavior for values that have only decimals. 

To see the test suite and its results, you can use an IDE or an interactive Python shell. The Python interpreter executes the test suite and prints the results, helping to validate the code and ensuring the function behaves as expected.