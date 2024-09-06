```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

#Test case 1: Basic increment
test_case1 = [1, 2, 3]
result1 = incr_list(test_case1)
assert list(result1) == [2, 3, 4]

#Test case 2: Different list type
test_case2 = 'abc'
result2 = incr_list(test_case2)
assert isinstance(result2, str) and result2 == 'abc' 

#Test case 3: List with sublists
test_case3 = [[1, 2, 3], [4, 5, 6]]
result3 = incr_list(test_case3)
assert list(result3) ==  [[2, 3, 4], [5, 6, 7]]

#Test case 4: List with recursive call
test_case4 = [0, 1, 2]
result4 = incr_list(test_case4)
assert list(result4) == [1, 2, 3]

#Test case 5: List with complex structure
test_case5 = [['a', 1, 2], [3, 'bc'], [4, 5, 6]]
result5 = incr_list(test_case5)
assert list(result5) ==  [2, 3, 4, 5, 'bc', 6]
```
The code defines a function `incr_list` that takes a list `l` as input and returns a new list with elements incremented by 1. The function is tested with five test cases, which cover basic increment, handling different data types, nested lists, and lists with complex structures.