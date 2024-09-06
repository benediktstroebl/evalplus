```python
def incr_list(lst):
    lst[:] = [lst[-1] + 1]
    return lst

# Test function for incr_list
def test_incr_list():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert incr_list(lst) == [6, 3, 6, 4, 6, 4, 10, 1, 124]

# Driver code
if __name__ == "__main__":
    test_incr_list()
```