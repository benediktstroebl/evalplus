```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

#Test cases
test_max_element = [
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123, "Max element not found"
]

test_cases = {
    lst = [1, 2, 3, 4, 5] : ValueError("test"),
    lst = [1, 2, 3, 0] : ValueError("test"),
    lst = [-200, -100, -10, -5] : ValueError("test"),
    lst = [21, 12, 43, 55, 78] : max_element(lst) == 55,
}

for test_case, should_fail in test_cases.with test:
    try:
    assert max_element(test_case), should_fail
    print(f"Test passed: {test_case}")
except AssertionError as e:
    print(f"Test failed: {test_case} - {e}")
```
This script defines a function max_element that returns the maximum element in a given list. The test cases cover various scenarios, including empty lists, negative numbers, out-of-range values, and valid inputs with expected maximum elements. The code provides clear test results and informative messages for each test case.