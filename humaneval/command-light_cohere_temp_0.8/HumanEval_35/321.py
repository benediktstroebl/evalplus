```python
def max_element(lst):
    if not_is_number(lst) and len(lst) == 0:
        return None
    if not_is_number(lst):
        return "Input should be a list of numbers"
    max_element = lst[0]
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element

# Unit tests
test_max_element = [
    demand("Function max_element returns the maximum element of the list correctly.", lambda: max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
]
``` 
This script defines a function max_element that takes a list as input and returns the maximum element in the list. It also has a tests on the correctness of the function.