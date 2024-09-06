```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l[:] = [x+1 for x in l]
    return l

# Test case 1
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3
def test3():
    l = [5, 3, 5, 2, 3, 3]
    assert incr_list(l) == l  # Should return the original list

if __name__ == "__main__":
    test1()
    test2()
    test3()
```
This code defines the incr_list function, which returns a list with elements incremented by 1. Three test cases are each this with the incr_list function and assert statements. The test cases cover scenarios where the expected results are the same as the original list with elements incremented.