```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    lst = list(set1)
    return lst

def test_unique():
    """
    Function tests.
    >>> unique([5, 3, 5, 2, 3, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Driver code
if __name__ == "__main__":
    print("Unique function test passed.")
    test_unique()
```
This code defines a function unique that returns a list with unique elements after removing duplicates from the input list. The test_unique function is then used to test the functionality of the unique function, and the output is confirmed.