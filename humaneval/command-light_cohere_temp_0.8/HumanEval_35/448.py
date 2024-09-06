```python
def max_element(lst):
    if not_unique(lst):  # Check for empty list or list with duplicate elements
        return None
    max_ = lst[0]  # Assume the first element is the maximum
    for num in lst[1:]:
        if num > max_:
            max_ = num
    return max_

def test_max_element(test_list):
    expected = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    result = max_element(test_list)
    assert result == expected, "The maximum element is not found."

# Example usage:
test_data = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element(test_data)
```
This Python script defines a function max_element that finds the maximum element in a list. The function first checks if the list is empty or contains duplicate elements, and if so, returns None. It then iterates through the  elements in the list and compares them with the current maximum value. The first greater element is updated and returned. The test function test_max_element verifies that the function correctly finds the maximum element in a given list.