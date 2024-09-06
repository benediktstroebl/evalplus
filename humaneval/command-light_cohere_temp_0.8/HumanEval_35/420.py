```python
def max_element(lst):
    if not_elements(lst):  # Empty list
        return None
    max_element = max(lst, key=lambda x: x)
    return max_element

def not_elements(lst):
    return any(map(lambda x: not_element(x), lst)))

def _element(x):
    try:
        return int(x)
    except ValueError:
        return str(x)

# Test the function
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
```