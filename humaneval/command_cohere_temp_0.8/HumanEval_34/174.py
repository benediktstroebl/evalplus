```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in set function to remove duplicate elements, and the list function to convert the set back to a list. The sort function is then used to sort the unique elements. 

A markdown code block with a unit test is also included to demonstrate the function's behavior. The test lists duplicates and returns the list of unique elements. The function is designed to work with any list input, and the test ensures its functionality. 

Would you like to test-drive this code? Any further questions or feedback on solving this problem?
```python
def test_unique():
    """Test the unique function."""
    lst = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    assert unique(lst) == expected
```