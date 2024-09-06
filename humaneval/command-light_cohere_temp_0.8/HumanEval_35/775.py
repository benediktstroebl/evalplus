```python
def max_element(lst):
    if not_elements(lst):  # Checks for empty list
        return None
    return max(lst)

def not_elements(lst):
    if isinstance(lst, list) and len(lst) == 0:
        return False
    return True
```
The function `max_element` accepts a list `lst` and outputs the list's maximum element. It uses the strategy `if_elements` to determine whether the input is a list and returns `False` if it is empty. 
It returns `True` if the input is a list and is not empty.