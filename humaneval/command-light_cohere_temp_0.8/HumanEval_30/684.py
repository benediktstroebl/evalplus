```python
def get_positive(input_list):
    return [num for num in input_list if num >= 0]

# Test case 1
test_case_1 = [-1, 2, -4, 5, 6]
assert get_positive(test_case_1) == [2, 5, 6]

# Test case 2
test_case_2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert get_positive(test_case_2) == [5, 3, 2, 3, 9, 123]

# Test case 3 (Should raise IndexError)
test_case_3 = []
with pytest.assert expected_error=IndexError:
    get_positive(test_case_3)
```
The Python script defines a function `get_positive` that filters out negative numbers from an input list, returning a new list with only the positive values. The test cases demonstrate that the function's expected behavior. The code also uses pytest to automate tests, providing more structured and readable test code.