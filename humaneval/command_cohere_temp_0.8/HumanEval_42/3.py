Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function uses a list comprehension to increment each element in the input list by 1 and provide a result. It avoids any repeated operations and optimizes the code for simplicity and efficiency. 

You can test this function with example tests provided in the problem statement. Simply write your unit tests in the same file using the `pytest` framework, and they will automatically execute when you run the file. For example:
```python
# Test incr_list function
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This will run the `incr_list` function with the given tests and assert that the results are as expected.  If the assertions pass, you will see an indication that the tests were successful, and in the case of failure, you will get descriptions for the failing assertions.  This makes debugging easier by pinpointing where the code does not behave as expected.