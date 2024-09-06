```python
def max_element(lst):
    if not_max_found(lst):
        return lst[-1]
    else:
        return max(lst, key=get_max_element_key(lst))

def get_max_element_key(lst):
    return max(
        key for key, value in enumerate(lst, 1) if not lst[key - 1] or value
    )

def not_max_found(lst):
    return all(v < lst[-1] for v in lst)
```
The function max_element takes a list lst as input and returns the maximum element in the list. Using a binary search approach, it first checks if there's a key in the list with a value greater than all the keys before. Then, it iterates through the list, and keeps track of the key with the highest value. This process continues until all largest value in the list is found or until all the keys have been checked.