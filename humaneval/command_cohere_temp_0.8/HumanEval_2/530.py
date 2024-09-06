```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Test cases
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(0.1) == 0.0
assert truncate_number(100.245) == 0.245
``` 
This script defines the `truncate_number` function, which takes a single parameter, `number`, and returns the decimal part of that number. To do this, it simply subtracts the integer part of `number` (obtained using the `round()` function) from `number` itself, effectively removing the integer part of the decomposition. The assertion tests assert that the function behaves as expected with different input cases. 
The function documentation is also added to explain the purpose and expected behavior of the function.