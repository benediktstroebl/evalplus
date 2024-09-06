```python
def max_element(lst):
    if not_elements(lst):  # Check for empty list
        return None
    
    max_ = lst[0]  # Initialize with first element
    for num in lst[1:]: 
        if num > max_: 
            max_ = num 
    return max_

def not_elements(lst):
    return len(lst) == 0

# Example
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(my_list))  # Output: 123
print(max_elements(my_list))  # Output: 0 (empty list)
```
The code defines a function `max_element` that takes a list as input and returns the maximum element in the list. The `not_elements` function is used to check for the existence of the list and returns `True` if it's empty. If the list is not empty, the function iterates through the list and compares each element with the current maximum value. The maximum element is then updated and returned.

The code also includes a related function `not_elements` to check for the existence of the list, which is useful to ensure that the input is a list and not an empty list.