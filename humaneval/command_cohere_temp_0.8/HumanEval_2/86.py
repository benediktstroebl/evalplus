```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Test cases
assert truncate_number(3.5) == 0.5
assert truncate_number(7.8) == 0.8
assert truncate_number(2.0) == 0.0
``` 

The test cases are also provided to validate the correctness of the `truncate_number` function. You can use these test cases as a starting point to ensure that the function behaves as expected under different scenarios. Test cases are an important part of writing robust code, as they help catch errors and ensure that the code behaves as expected.  If you encounter any problems or have any further questions related to testing or any other coding concepts, please don't hesitate to ask!