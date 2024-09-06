```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1: Basic list increment
test_case1 = [1, 2, 3]
result_case1 = incr_list(test_case1)
assert result_case1 == [2, 3, 4]

# Test case 2: List with repeated elements
test_case2 = [5, 3, 5, 2, 3, 3]
result_case2 = incr_list(test_case2)
assert result_case2 == [6, 4, 6, 3, 4, 4, 10]

# Test case 3: List with mutable element
test_case3 = ['a', 'b', 'c']
result_case3 = incr_list(test_case3)
assert result_case3 == ['a', 'b', 'c', 'd']

# Test case 4: List with custom element
test_case4 = [1, 2, 3, 'custom']
result_case4 = incr_list(test_case4)
assert result_case4 == [2, 3, 'custom']
```
The function `incr_list` takes a list `l` as an argument and uses a list comprehension with a linear increment to return a new list with elements incremented by 1. The test cases cover a basic list increment, lists with repeated elements, lists with mutable elements, and lists with custom elements. The `assert` statements at the each test case ensure that the `incr_list` function produces the expected result.