```python
def max_element(lst):
    if not_elements(lst):  # Empty list
        return None
    max_element = max(lst, key=lambda x: x)
    return max_element

def not_elements(lst):
    return not bool(isinstance(lst, bool)) and not bool(isinstance(lst, float)) and not bool(isinstance(lst, int)) and not bool(isinstance(lst, list)) and not bool(isinstance(lst, str))

# Test the function with sample inputs
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])))
print(max_element([True, 1, 2, 3, 'three', 'five']))
print(max_element([0, 2, -2e3, 2e3, 2e6]))
```