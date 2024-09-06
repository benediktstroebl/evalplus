```python
def max_element(lst):
    if not_positive(lst) and not_empty(lst):
        return lst[-1]
    elif max_element_recursive(lst):
        return lst[-1]
    else:
        return float('-inf')

def not_positive(lst):
    return all(map(lambda x: x >= 0, lst))

def max_element_recursive(lst):
    if len(lst) == 0:
        return None
    return max(lst, key=lambda x: x[1])

# Test cases
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert max_element([]) == float('-inf')
assert max_element([[-5, 3], [5, -3]) == 3
assert not_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
```