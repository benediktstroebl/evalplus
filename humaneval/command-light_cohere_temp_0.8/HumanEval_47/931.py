```python
def median(l):
    """Return median of elements in the list l."""
    return (len(l) + 1) / 2.0

def test_median():
    """
    Unit test for median function.
    It verifies that the calculates the correct median for different lists and returns ValueError for invalid inputs.
    """
    list1 = [10, 20, 30, 40]
    assert median(list1) == 30.0

    list2 = [10, 20, 40, 50]
    assert median(list1) == 35.0

    list2 = [-10, 4, 6, 1000]
    try:
        assert median(list) == 15.0
        except: raise ValueError("test failed")
    list2 = [3, 1, 2, 4]
    try:
        assert median(list2) == 4.0
    except: raise ValueError("test failed")
```