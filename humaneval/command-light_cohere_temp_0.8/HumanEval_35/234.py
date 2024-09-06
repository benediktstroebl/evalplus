```python
def max_element(lst):
    if not_len(lst):
        return None
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val

def test_max_element(test_list):
    expected = [1, 2, 3, 5, 123]
    got = max_element(test_list)
    assert got == expected, f"Expected: {expected}, Got: {got}"

# Example 1
test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element(test_data)

# Example 2
test_data2 = [5, -5, 2]
test_max_element(test_data2)
```
The code defines a `max_element` function that takes a list as input and finds the maximum element in the list. It uses an iterative approach where the maximum element is the first element in the list, it compares each element with the current maximum value and updates the maximum accordingly. 

The `test_max_element` function takes a list of test cases and calls the `max_element` function with it. The function then compares the expected maximum element with the one returned by the `max_element` function and raises an `AssertionError` if they do not match.