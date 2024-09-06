```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([x for x in l if not (x in seen or seen.add(x))])
```

This script defines a function unique that takes a list l as input and returns a list of unique elements from l, sorted in ascending order. The function uses a set seen to keep track of already-seen elements in the input list. The function then iterates over the input list, and for each element x, it checks if x is already in the set seen. If not, it adds x to the set seen and includes x in the output list. If x is already in the set seen, it skips x and continues iteration. Finally, the function returns the output list containing all unique elements from l, sorted in ascending order. 
```python
def test_unique():
    """Test the unique function"""
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    assert unique([1, 1, 2, 3, 4, 4, 4]) == [1, 2, 3, 4]
    assert unique([1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == [1, 2, 3, 4]
```

The script also includes test code to verify the function unique solution. The test code includes three assert statements with input lists and expected output lists. The assert statements compare the output of the unique function for the input lists against the expected output lists.

When executed, the test code runs the unique function with the input lists and verifies that the actual output matches the expected output. Overall, the code provides an accurate, efficient, and tested solution to the problem.