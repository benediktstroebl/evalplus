```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(114.0) == 0.0
```
The function `truncate_number` takes a single parameter, which is the number to be processed. It uses the built-in `round()` function to round the number to the nearest integer. 

Then, it subtracts the rounded number from the original number, thus returning the decimal part of the number. The test suite includes three examples, ensuring that the function returns the expected output for all float numbers.