```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test cases
def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    assert max_element(test_list) == expected

# Another test with negative numbers
test_another = [-5, -10, -3, -20]
expected_another = -20
assert max_element(test_another) == expected_another
```
This code defines a function max_element that finds the maximum element in a given list. It also provides test cases to test the function's behavior.