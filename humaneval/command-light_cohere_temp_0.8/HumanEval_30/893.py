```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Unit tests
test_get_positive = []
test_get_positive.py  = [ [
    -1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [True, True, True, False, False, True, True, False, True]

def test():
    """Individual function to test the get_positive function"""
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    assert not get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [False]
    assert get_positive([123, 0, 9, 2]) == [123, 0, 9, 2]

# Run the unit tests
test()
 ```