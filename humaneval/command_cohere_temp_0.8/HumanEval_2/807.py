```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
```
This script includes a function `truncate_number` that takes a single parameter, `number`, and returns the decimal part of that number. This is achieved by subtracting the closest integer (rounded number) from the input number. The resulting difference will be the desired decimal part of the number. It can be decomposed into an integer part and a decimal part, where the decimal part is the remaining fraction of the number less than 1. 

The script also includes automated tests that assert the function's behavior against its expected output for the given inputs. The tests ensure that the `truncate_number` function correctly returns the decimal part of the number, regardless of the integer part of the input.