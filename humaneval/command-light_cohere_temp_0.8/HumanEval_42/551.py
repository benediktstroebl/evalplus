```python
def incr_list(lst):
    lst[:] = [1] + lst  # Prepend 1 to each element
    return lst

# Test
def test_incr_list(test_lst):
    lst = incr_list(test_lst)
    for item in lst:
        assert item == (item + 1), f"expected {item + 1}, got {item}"
    return lst == [1, 2, 3]

test_incr_list([5, 3, 5])
test_incr_list([1, 2, 3]) # Should pass

# Output
```