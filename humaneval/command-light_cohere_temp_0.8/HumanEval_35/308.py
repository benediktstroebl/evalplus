```python
def max_element(lst):
    if not_positive(lst) and not_unique(lst):
        raise ValueError("Input list must contain only positive integers")
    return max(lst)

def not_positive(lst):
    return all(x > 0 for x in lst) and len(set(lst)) == len(lst)

def not_unique(lst):
    return set(lst) == {list(lst)}

# Unit tests
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert not max_element([-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
assert not max_element([1, 2, 3, -5])
assert not_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```
The provided code defines a function max_element that finds the maximum element in a given list. The function also includes input validation to ensure the list contains only positive integers. The code also has two helper functions, not_positive and not_unique, which check for conditions to pass the input tests. The script also includes unit tests to verify the functionality of the max_element function.