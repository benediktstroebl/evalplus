```python
def max_element(lst):
    if not_elements(lst):  # Base case
        return None
    max_element = lst[0]  # Initialize the element with the first value
    for i in lst[1:]:  # Compare all elements to the current maximum
        if i > max_element:  # Update the element if a greater element is found
            max_element = i
    return max_element

def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected_result = 123
    result = max_element(test_list)
    assert result == expected_result, f"Expected: {expected_result}, But got: {result}"

# Run the tests
test_max_element()
 ```
The function max_element returns the maximum element in a list. The function first compares the the element of the list with the current maximum element. If the current element is greater than the maximum element, the current maximum element is updated. The function then iterates over all the remaining elements of the list and compares each element to the current maximum element. 

This function can be used to find the maximum element in any list of numbers.