```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

#Test cases
test_incr_list = []
test_incr_list.append([1, 2, 3])
test_incr_list.append([5, 3])
test_incr_list.append([5, 4])

def test_function(test_cases):
    """To test the incrementer function."""
    for case in test_cases:
        l = [1, 2, 3]
        result = incr_list(l)
        assert len(result) == 5
        assert result == [2, 3, 4]

#Main execution
test_incr_list = test_function([1, 2, 3])
test_incr_list.assert print(test_incr_list)
```