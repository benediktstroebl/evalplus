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
assert truncate_number(100.001) == 0.001
``` 

This script includes a test suite with several test cases to ensure the `truncate_number` function works as expected. You can use these test cases as a starting point to ensure correctness against different scenarios. Feel free to add more test cases as required, especially edge cases, to exercise the function and reinforce its reliability. 
If you face any issues or have further questions related to the problem or any other topic, please don't hesitate to ask.