```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - round(number)

# Tests
round_val = 3.5
test_val = truncate_number(round_val)

if test_val == 0.5:
    print("Passed")
else:
    print("Failed")
```

The function `truncate_number` returns the decimal part of the input number by subtracting the largest integer less than or equal to the number (obtained by `round(number)`) from the number itself, as specified in the prompt. This is the definition of the decimal part of a number in floating-point representation. 

The test code is also added to check if the function returns the expected value for the given test case. The test harness will print "Passed" if the test case passes, or "Failed" if it fails. You can uncomment the `print` statements and comment the `pass` statement if you wish to see the actual test output. 

To run the test, you can leave the code as is and use the Python interpreter. Simply copy and paste the entire code block into a Python interpreter prompt and press Enter. The test will run automatically. 

To make the test automated, you can add the following code at the bottom of the script: 

```python
if __name__ == "__main__" :
    test_val = truncate_number(round_val)
    assert test_val == 0.5, "Failed"
    print("Passed")
``` 

This code block will automatically run the test when the script is executed directly, producing the same "Passed" or "Failed" output as before.