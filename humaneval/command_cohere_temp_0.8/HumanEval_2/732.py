```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```
This function simply takes a number and returns the decimal part of the number. This is accomplished by finding the difference between the number and the integer part of the number. For example, if the number is 3.5, then the integer part is 3 and the decimal part is 0.5. So, the function would return 0.5. 

Here is a simple test case to confirm the functionality of the function:
```python
test_cases = [(3.5, 0.5), (2.7, 0.7), (1.5, 0.5), (0.1, 0.1)]
for number, expected in test_cases:
    result = truncate_number(number)
    assert result == expected, f"For number {number}, the expected decimal part {expected} does not match the result {result}"
``` 
This will verify that the function produces the expected result for a variety of test cases. 

This approach is straightforward and simple, exhibiting Pythonic simplicity, which is ideal for beginners and for tasks that require minimal complexity.