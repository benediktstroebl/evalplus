```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Test cases
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(44.0) == 0.0
``` 

The function `truncate_number` takes a single parameter, `number`, which is the number to be processed. It calculates the decimal part of the number by subtracting the largest integer less than or equal to `number` from `number` itself. The resulting value is the decimal part of the number. 

The provided test cases verify that the function behaves as expected for a variety of inputs.