```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test 1
test_cases = [ [5, 3, 5, 2, 3, 3, 9, 0, float('inf'), 123], [5, [2, 3, 5], [9, 0, 123]]]
for test_case in test_cases:
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9, 123]
    assert actual == expected

# Test 2
test_cases = [5, 3, 5, 2, 3, 3, 9, 0, [1, 2], [123]]
for test_case in test_cases:
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9]
    assert actual == expected
```
This script defines a function called unique that takes a list as an argument and returns a new list with unique elements from the original list. It uses a fact to keep track of unique elements seen so far and only adds elements that are not duplicates and not equal to infinity. The test cases cover a expected behavior of the function. The test cases are defined as lists of values and the function is called with each test case to check if the output is correct.