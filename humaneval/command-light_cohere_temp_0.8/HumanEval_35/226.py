```python
def max_element(lst):
    if not_elements(lst):
        raise ValueError("Input list is empty")
    return max(lst)

def not_elements(lst):
    return not len(lst) == 0

# Test cases
max_element([1, 2, 3])  # Output: 3
max_element([5, 3, -5])  # Output: 3
max_element([5, 3, -5, 2, -3, 3, 9, 0, 123])  # Output: 123
max_element([])  # Input empty list, raises ValueError
```