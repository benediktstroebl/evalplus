```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

#Test case 1
test_cases = [1, 2, 3]
assert incr_list(test_cases) == [2, 3, 4]

#Test case 2
test_cases = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert incr_list(test_cases) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

#Test case 3 (edge case)
test_cases = [0, 2, 3]
assert incr_list(test_cases) == [0, 2, 3]
```