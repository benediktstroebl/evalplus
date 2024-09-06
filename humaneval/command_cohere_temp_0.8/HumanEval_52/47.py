```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each element in the input list `l` and compare each element with the threshold value `t`. 
The result of the comparison is a Boolean value, which is then returned to indicate whether all elements in the list are below the threshold value or not. 
If all elements are less than the threshold, the function returns `True`, otherwise, it returns `False`. 

Here is a test case that verifies the correct operation of the function:
```python
def test_below_threshold():
    assert below_threshold([1, 2, 4, 10], 100) == True
    assert below_threshold([1, 20, 4, 10], 5) == False
```
This test case uses the `assert` statement to check whether the output of the `below_threshold()` function is correct or not. 
If the condition is true, the assertion passes, otherwise, it would raise an `AssertionError` indicating that a bug has occurred.