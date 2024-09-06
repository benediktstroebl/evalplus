Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. The returned result is then assigned to the list `result`. 

To test this function, you can call it with various input lists and verify that the output is correct. Here is an example of how you can test this function with different inputs:
```python
# Test 1
input_list = [1, 2, 3]
expected_result = [2, 3, 4]
result = incr_list(input_list)
assert result == expected_result

# Test 2
input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
expected_result = [6, 4, 6, 3, 4, 4, 10, 1, 124]
result = incr_list(input_list)
assert result == expected_result
```
These tests ensure that the `incr_list` function works correctly for different scenarios. 
The `assert` statement will raise an error if the assertion fails, indicating that the function has not performed as expected. 
Ensure that you have the required testing dependencies installed, if not, you can do so with:
```
pip install pytest
``` 
This way, you can confidently use and rely on the `incr_list` function to increment elements in a list by 1.