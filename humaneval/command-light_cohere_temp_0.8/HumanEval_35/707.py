```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test case 1
test_case_1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_case_1) == 123

# Test case 2
test_case_2 = [1, 2, 3]
assert max_element(test_case_2) == 3
```
The function max_element uses the built-in Python function max to return the maximum element in the list. In the above code, test_case_1 contains a list with various values, and the test_case_2 list contains only positive integers. 
The function has also been successfully tested with the test cases provided.