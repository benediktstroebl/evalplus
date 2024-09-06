```python
def max_element(lst):
    if not_elements(lst):  # Test for empty list
        return None
    if len(lst) == 1:  # Handle special case: single element list
        return lst[0]
    max_num = max(lst)  # Initialize max element with the maximum of the list
    return max_num

def not_elements(lst):
    if not lst:  # Test for empty list
        return False
    if len(lst) == 0:  # Test for empty list
        return True
    return len(lst) > 1
```