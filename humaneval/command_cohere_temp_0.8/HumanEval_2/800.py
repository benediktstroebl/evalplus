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
This code snippet defines a function `truncate_number` which takes in a single parameter, `number`, and returns the decimal part of the number by subtracting the closest integer to it. 
To test the functionality of the `truncate_number` function, two tests are included. The first test asserts that the function returns 0.5 when the input is 3.5. The second test asserts that the function returns 0.8 when the input is 7.8. 

This code demonstrates how to extract the decimal part of a floating-point number and tests essential aspects of writing robust code, including function definition, testing, and documentation.