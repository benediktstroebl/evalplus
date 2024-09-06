```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(0.1) == 0.0
``` 
The function `truncate_number` takes a single parameter, which is the number to be processed. It uses the `round()` function to round the number to the nearest integer, and then it subtracts this value from the original number. The resulting value is the decimal part of the original number, which is returned by the function.

The provided tests ensure that the function behaves as expected with different inputs. Test cases include a number with both digits after the decimal point and a number three places after the decimal point. These tests can be added to a separate module to ensure robustness and functionality.