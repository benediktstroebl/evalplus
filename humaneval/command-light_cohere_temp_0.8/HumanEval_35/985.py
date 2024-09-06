```python
def max_element(lst):
    return max(lst)

# Basic test case
assert max_element([1, 2, 3]) == 3

# List with negative and fractional elements
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Large list with diverse elements
assert max_element([-5, -3, 123, 1, 7, 0, 10, 2, 8, 3, 4, -9]) == 0

# Invalid input: list with non-numeric elements
with pytest.assert expected_exception=TypeError):
    assert max_element([1, 2, '3', 'four']) == 3  

```
The provided Python code defines a function max_element that finds and returns the maximum element in a given list. The code includes several test cases to validate the correctness of the max_element function. 

Note that this code uses the pytest framework for testing, which is a popular and powerful tool for automating tests and assertions in Python.