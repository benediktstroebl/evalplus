```python
def below_threshold(l: list, t: int) -> bool:
    return all(x < t for x in l)
```
This function uses the `all()` function to iterate over each list element `x`, comparing it to the threshold `t`. The `all()` function returns `True` if all comparisons are `True`, indicating that all list elements are below the threshold, otherwise `False`. 

Here is a Markdown code block with corresponding test cases to verify the correct functionality of the function:
```python
def test_below_threshold():
    # Test case from the problem statement
    assert below_threshold([1, 2, 4, 10], 100) == True

    # Test case with non-true output
    assert below_threshold([1, 20, 4, 10], 5) == False

    # Edge case
    assert below_threshold([0, 0, 0, 0], 0) == False

    # Long list with mixed values
    assert below_threshold([1, 2, 3, 4, 5, 4, 3, 2, 1], 4) == True

    # Empty list
    assert below_threshold([], 100) == True

test_below_threshold()
``` 
This would ensure that the function `below_threshold` works correctly for different scenarios.