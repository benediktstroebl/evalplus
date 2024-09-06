Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a new list with its elements incremented by 1. It uses a list comprehension to iterate over each element in the input list and increments it by 1. 

Here's a markdown code block with a corresponding test to verify the function's behavior:
```python
def test_incr_list():
    """Test the incr_list function"""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

When you run this test, it will verify that the function `incr_list` behaves as expected with the provided examples in the comment. 
If you want to see the test execution results, you can append the following code at the end of the script:
```python
test_incr_list()
``` 
This will run the test case and provide you with an output of the test results.