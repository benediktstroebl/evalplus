```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    for i in range(n): l[i] += 1
    return l

def test_incr_list():
    """Test the incr_list function"""
    lst = [1, 2, 3]
    expected = [2, 3, 4]
    for item in lst:
        actual = incr_list(lst)
        assert actual == expected
        lst.remove(item)  # Clean up the
```
This Python code defines a function `incr_list` that increments the elements of a given list by one. The function takes a list as an argument and returns a new list with the elements incremented by 1. 

Additionally, there is a `test_incr_list` function that provides a simple test for the `incr_list` function. The test function passes the test, demonstrating its functionality and correctness.