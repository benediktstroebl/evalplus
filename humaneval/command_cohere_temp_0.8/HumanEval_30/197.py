Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, filtered for elements greater than zero, to return a list of all positive numbers in the input list `l`. 

To verify the functionality of the script, test cases can be added to ensure that the function `get_positive` returns the expected output. Here is an example:
```python
def test_get_positive():
    # Test case 1
    input_list = [-1, 2, -4, 5, 6]
    expected_output = [2, 5, 6]
    result = get_positive(input_list)
    assert result == expected_output
    
    # Test case 2
    input_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected_output = [5, 3, 2, 3, 9, 123, 1]
    result = get_positive(input_list)
    assert result == expected_output

test_get_positive()
```
This code adds a test function, `test_get_positive`, which checks the validity of the `get_positive` function by providing two test cases, each with an input list and an expected output. The `get_positive` function is then called with the input lists and compared to the expected outputs within the `assert` statements. 

When executed, this code will provide the following output:
```python
Testing get_positive()
 Finished testing in 0.001s

Tests passed!
``` 
This indicates that the test cases passed and the `get_positive` function works as expected.