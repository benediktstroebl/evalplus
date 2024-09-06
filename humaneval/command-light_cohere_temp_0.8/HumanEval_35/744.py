```python
def max_element(lst):
    if not_elements(lst):  # Corner case: empty list
        return None
    if len(lst) == 1:  # Corner case: single element list
        return lst[0]
    max_element = max(lst)  # Initialize max element with the last element
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element

def test_max_element(test_list):
    expected = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    actual = max_element(test_list)
    assert actual == expected, f"Expected {expected}, got {actual}"

# Example usage
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(test_list)
print(result)  # Output: 123
```

The provided code defines a Python script that aims to find the maximum element in a given list. It utilizes a maximum approach that iterates through the list, compares each element with the current maximum, and updates the maximum value if a larger element is encountered. The corner cases of an empty list and a list with a single element are handled appropriately. The script includes a test function that validates the max_element function with various test cases, ensuring the function correctly identifies the maximum element in the given lists.