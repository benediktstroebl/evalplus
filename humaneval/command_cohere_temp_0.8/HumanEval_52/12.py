```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True`, indicating that all list elements are below the threshold, otherwise `False`. 

Here is a markdown code block with a simple test to verify the functionality of the function:
```python
def test_below_threshold():
    assert below_threshold([1, 2, 4, 10], 100) == True
    assert below_threshold([1, 20, 4, 10], 5) == False
```
This test verifies that the `below_threshold` function works correctly with different input cases. 
To run this test, you can copy this code into a Python file and run it using the `python -m unittest test_below_threshold` command.

This way, the code snippet provided solves the problem and passes the given tests, and can be executed independently.