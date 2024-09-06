```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Test cases
test_incr_list = []
test_incr_list.push([1, 2, 3])
test_incr_list.push([5, 4])
test_incr_list.push([5, 5])
test_incr_list.push([6, 6])
test_incr_list.push([7])

def test_function(test_case: list):
    assert list(incr_list(test_case)) == [2, 3, 4]
    assert list(incr_list(test_case)) == [6, 5, 6]
    assert list(incr_list(test_case)) == [7]
    assert test_case[0] == 1
    assert test_case[2] == 2
    assert test_case[5] == 6
    assert test_case[7] == 7
test_incr_list = test_function(test_incr_list)
print("Tests passed!")
```