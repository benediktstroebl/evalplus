```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
number = 3.5
test_result = truncate_number(number)

if test_result == 0.5:
    print("Passed")
else:
    print("Failed")
``` 

The function `truncate_number()` returns the decimal part of the input number by subtracting the nearest integer from the original number, effectively capturing the remaining decimal amount. 

This approach leverages Python's implicit casting of floating-point numbers to integers, committing the rounding action. The test scenario follows, verifying if the computed result matches the expected value of 0.5. 

To ascertain the test's outcome, the script employs a conditional statement to showcase either a 'Passed' or 'Failed' message, contingent on the test's result. 

Please feel free to adapt this code to your needs or explore other troubleshooting scenarios. 
If you have further questions or need additional assistance, please don't hesitate to ask!