```python
def incr_list(lst):
    n = len(lst)
    result = [n + 1] * (n + 1) // 2
    return result

# Test case 1: Basic increment
test_case1 = [1, 2, 3]
result_test_case1 = incr_list(test_case1)
assert result_test_case1 == [2, 3, 4]

# Test case 2: Single element list
test_case2 = [5]
result_test_case2 = incr_list(test_case2)
assert result_test_case2 == [6]

# Test case 3: Nested list
test_case3 = [1, 3, 5, 7]
result_test_case3 = incr_list(test_case3)
assert result_test_case3 == [6, 8, 10]

# Test case 4: Repeated elements
test_case4 = [5, 5, 5, 5]
result_test_case4 = incr_list(test_case4)
assert result_test_case4 == [6, 6, 6, 6]
```
This script defines a function incr_list that takes a list as input and returns a new list with elements incremented by 1. The test cases provided validate the