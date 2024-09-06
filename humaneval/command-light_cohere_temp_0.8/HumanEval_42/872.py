```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    l.append(2)
    l.append(3)
    return l

def test_incr_list():
    """Test the incr_list function"""
    l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert incr_list(l) == [6, 3, 6, 4, 6, 4, 4, 10, 1, 124]
    return incr_list(l) == [6, 3, 6, 4, 6, 4, 4, 10, 1, 124]

# Run the function and test the result
print(test_incr_list())
```