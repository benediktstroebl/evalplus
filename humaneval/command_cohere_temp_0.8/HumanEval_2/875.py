```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply converts the parameter to an integer (rounded down), and then returns the difference between the original number and the integer. The resulting difference will be the fractional part of the original number, which is the desired output. 
The function is self-contained, meaning it does not rely on any external dependencies or statements that are not included in the code block itself. 

Here is a test case that can be used to validate the functionality of the function:
```python
test_case = 3.5
expected_output = 0.5
result = truncate_number(test_case)
assert result == expected_output
```
The output of this test case will be 0.5, which is the decimal part of the number 3.5. 

Let me know if I have misunderstood the problem statement and if I should adjust the function to fulfill the actual requirements. Feel free to also clarify whether the emphasis lies on the function returning the decimal part or if the problem intended to extract the integral part of the input number.