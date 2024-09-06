```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test case 1:
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2:
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]

# Test case 3:
def test3():
    l = [5, 3, 5, 2, 3, 3]
    assert incr_list(l) == l

if __name__ == "__main__":
    test1()
    test2()
    test3()
```
The function `incr_list` takes a list `l` as input and returns a new list with elements incremented by 1. The test cases verify that function's correctness by creating lists with specific values and comparing the returned lists with the original ones.