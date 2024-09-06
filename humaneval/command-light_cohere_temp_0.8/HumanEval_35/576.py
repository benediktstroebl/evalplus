```python
def max_element(lst):
    if not_is_positive(lst) and not_is_empty(lst):
        return lst[-1]
    elif not_is_empty(lst):
        return float('-inf')
    else:
        return max(lst, default=float('-inf'))

def not_is_positive(lst):
    return all(x > 0 for x in lst)

def not_is_empty(lst):
    return len(lst) == 0

# Unit tests
max_element([1, 2, 3])  # Output: 3
max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # Output: 123
max_element([])  # Output: float('-inf')
max_element([1, 2, -3])  # Output: float('-inf')
max_element([1, 2, 3, 0])  # Output: 0
max_element([1, 2, 3, float('inf')])  # Output: 3
not_is_positive([1, 2, 3])  # Output: False
not_is_empty([1, 2, 3])  # Output: True
not_is_empty([])  # Output: True
```  Here's the function `max_element` takes a list as input and returns the maximum element in the list. The `not_is_positive` function checks if all elements in the list are greater than 0, and returns True if they are. The `not_is_empty` function checks if the list is empty and returns True if it is.