```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]  # Return the list with a single appended element, then add another 1 to keep the sequence ongoing 

# Test case 1:
def test1():
    return assert_list(incr_list([5, 3, 5]))  # Should return [6, 5, 6]

# Test case 2:
def test2():
    assert_list(incr_list([1, 2, 3])) == [2, 3, 4]  # Should return the list with elements incremented by 1 

# Test case 3:
def test3():
    assert_list(incr_list([9, 0, 123])) == [10, 1, 124]  # Should return the list with elements incremented by 2 

# Test case 4:
def test4():
    assert_list(incr_list([7, 8, 9])) == [8, 9, 10]   # Should return the list with elements incremented by 1