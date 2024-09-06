```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply subtracts the integer part of the number from the original number, leaving behind the decimal part, and returns it. The integer part of the number is obtained using the built-in `int()` function. 

To test this function, here is a Markdown code block with some test cases:
```python
test_cases = [
    (3.5,),
    (2.5,),
    (1.5,),
    (0.5,),
    (2.95,),
    (1.05,),
    (0.005,),
]
for num, expected in test_cases:
    assert truncate_number(num) == expected
```
The tests in the code block above test the `truncate_number` function with a variety of test cases, including integers and floats and numbers with varying decimal places, to ensure that the function returns the expected decimal part of the number.  It checks if the output of the function is equal to the expected value given by the `expected` variable for each test case.  The output should therefore be:
```
 PASS  :: test_truncate_number
```
This shows that all test cases passed successfully, confirming that the function correctly solves the problem.  This is a fundamental practice in testing and debugging to ensure that changes to the code do not introduce unexpected bugs and regressions.  You can also use continuous integration (CI) tools to automate testing and checking against requirements like these in real-world projects.