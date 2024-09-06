```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test the function with various inputs
# Test case 1: Basic input
test_case_1 = [1, 2, 3]
result_case_1 = incr_list(test_case_1)
assert result_case_1 == [2, 3, 4]

# Test case 2: List with many elements
test_case_2 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result_case_2 = incr_list(test_case_2)
assert result_case_2 == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3: List with complex structure
test_case_3 = [0, 123, [1, 2], [3, 4, 5]]
result_case_3 = incr_list(test_case_3)
assert result_case_3 == [6, 4, 6, 3, 4, 4, 10]

# Test case 4: Nested list with custom element
test_case_4 = [0, 1, [2, 3], [4]]
result_case_4 = incr_list(test_case_4)
assert result_case_4 == [6, 4, 6, 3, 4]

# Error handling for non-list input
try:
    incr_list("hello")
except TypeError:
    print("Input is not a list.")
```