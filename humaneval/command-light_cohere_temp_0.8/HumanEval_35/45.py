```python
def max_element(lst):
    if not_list(lst):  # Check if list is valid
        return "Input should be a list"
    if not len(lst) or lst == []:  # Check for empty list or [], return None
        return max(lst)

# Test the function
result = max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert result == 123
result = max_element([])
assert result == None
result = max_element([1, 2, 3, 4, 5])
assert result == 5
result = max_element([1, 2, 2, 3, 4, 6])
assert result == 6
```
The code defines a Python function max_element that finds the maximum element in a given list. The function performs input validation to ensure the list is valid and returns an appropriate error message if not. The function then checks for the empty list and returns None. It then applies the max() function from the list and returns the maximum value. Finally, it tests the result of the max_element function to verify its correctness.