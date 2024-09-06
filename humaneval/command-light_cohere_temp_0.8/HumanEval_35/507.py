```python
def max_element(lst):
    if not_elements(lst):  # Handle empty list
        return None
    max_element = max(lst, key=lambda x: x)
    return max_element

def not_elements(lst):
    return not len(lst) == 0

# Test the function
list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
max_result = max_element(list1)
print("Maximum element:", max_result)

list2 = [-10, 123, -5, -20]
max_result2 = max_element(list2)
print("Maximum element:", max_result2)
```
The above script defines the `max_element` function, which takes a list `lst` as input and returns the maximum element from the list. It also defines a essential utility function `not_elements` to handle the edge case of an empty list. The `not_elements` function returns `True` if the list is empty, which allows the `max_element` function to handle this case without raising an error.