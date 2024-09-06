```python
def max_element(lst):
    return max(lst)

# Test cases
test_max_element = [
    [1, 2, 3],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [5, 7, 3, -9, 11, 1, -33, -100]
]

for test_case in test_max_element:
    assert max_element(test_case) == max(test_case)
```
This function `max_element` takes a list `lst` as an argument and returns the maximum element in that list using the `max()` built-in function. The test cases demonstrate that this function's functionality. The `assert` statements are used to check the correctness of the function's output.